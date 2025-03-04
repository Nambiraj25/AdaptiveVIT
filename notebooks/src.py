import timm
import torch
from torch import nn
from torchvision import transforms, datasets
from torch.utils.data import DataLoader, ConcatDataset, Subset

class Adapter(nn.Module):
    def __init__(self, in_features, reduction_factor=4):
        super().__init__()
        self.adapter = nn.Sequential(
            nn.Linear(in_features, in_features // reduction_factor),
            nn.GELU(),
            nn.Linear(in_features // reduction_factor, in_features)
        )
        
    def forward(self, x):
        return x + self.adapter(x)
    
class ViTWithAdapters(nn.Module):
    def __init__(self, num_domains=4, num_classes=7):
        super().__init__()
        self.vit = timm.create_model('vit_base_patch16_224', pretrained=True)

        for param in self.vit.parameters():
            param.requires_grad = False
            
 
        self.num_domains = num_domains
        self.adapters = nn.ModuleList()

        for _ in range(num_domains):
            domain_adapters = nn.ModuleList()
            for block in self.vit.blocks:
          
                adapter_mhsa = Adapter(768)
                adapter_ffn = Adapter(768)
                domain_adapters.append(nn.ModuleDict({
                    'adapter_mhsa': adapter_mhsa,
                    'adapter_ffn': adapter_ffn
                }))
            self.adapters.append(domain_adapters)
        
      
        self.vit.head = nn.Linear(768, num_classes)
        
    def set_domain(self, domain_id):

        for block, adapters in zip(self.vit.blocks, self.adapters[domain_id]):
            block.adapter_mhsa = adapters['adapter_mhsa']
            block.adapter_ffn = adapters['adapter_ffn']

    def forward(self, x):
        return self.vit(x)
def load_pacs_splits(domain, train_ratio=0.8, subset_ratio=0.2):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    
    full_dataset = datasets.ImageFolder(
        root=f'/content/pacs/pacs_data/pacs_data/{domain}',
        transform=transform
    )
    
    
    subset_size = int(len(full_dataset) * subset_ratio)
    indices = np.random.choice(len(full_dataset), subset_size, replace=False)
    subset = Subset(full_dataset, indices)
    

    train_size = int(train_ratio * len(subset))
    val_size = len(subset) - train_size
    train_subset, val_subset = torch.utils.data.random_split(subset, [train_size, val_size])
    
    return train_subset, val_subset