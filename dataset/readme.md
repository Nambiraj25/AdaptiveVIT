# Data Directory

This folder contains instructions for acquiring and preparing the dataset required for **AdaViT: Adaptive Vision Transformers for Multi-Domain Image Recognition**. In this project, we use the **PACS dataset**.

## 1. Overview
The PACS dataset is a popular benchmark for domain generalization tasks. It contains images from four different domains:
- **Photo**
- **Art Painting**
- **Cartoon**
- **Sketch**

This dataset is used to evaluate the model's ability to generalize across various visual styles.

## 2. Dataset Details

### Dataset: PACS
- **Source**: Kaggle
- **Dataset Name**: pacs-dataset
- **Download Link/Command**:  
  You can download the dataset using the following Kaggle command:
  ```bash
  kaggle datasets download -d nickfratto/pacs-dataset
###Description:
The PACS dataset includes images organized by domain and class. It is extensively used in research for domain adaptation and generalization.
##3. Download and Extraction Instructions
Follow these steps to set up the PACS dataset in this data/ directory:

###Download the Dataset:
Execute the following command in your terminal (or in a notebook cell) to download the PACS dataset:

bash
kaggle datasets download -d nickfratto/pacs-dataset
Extract the Dataset:
After downloading, unzip the file using:

bash

unzip -q pacs-dataset.zip -d /content/pacs
If you're running locally, adjust the extraction path as needed.

###Set Permissions:
Ensure that the dataset folder has the correct permissions:

bash
chmod -R 755 /content/pacs
Modify the path if you're using a local setup.

###Organize the Data:
Move or copy the extracted folder (typically named pacs or similar) into this data/ directory. Your final structure should look like:

kotlin
Copy
Edit
data/
 └── pacs/
      ├── Photo/
      ├── Art_Painting/
      ├── Cartoon/
      └── Sketch/

##4. Preprocessing Steps

###Image Resizing:
Images may need to be resized as required by the model. Refer to the code in src.ipynb for details on the desired dimensions.

###Normalization:
Normalize images using the specified mean and standard deviation (e.g., those from ImageNet) or as configured in the project.

###Data Augmentation:
Data augmentations (such as random crops, flips, etc.) might be applied on the fly during training. Check the training pipeline in src.ipynb for specific augmentation strategies.

##5. Usage in the Project

###Data Path Configuration:
Ensure that the path in your configuration files (e.g., config.yaml in the src/ directory) points to the location of the PACS dataset (e.g., data/pacs).

###Training and Evaluation:
The scripts in src.ipynb and other code files automatically look for the dataset under the specified path. Make sure that the folder structure is maintained as described above.

##6. Troubleshooting

###File Not Found Errors:
Verify that the dataset is located in the correct directory and that the folder names match those expected by the code.

###Corrupted Downloads:
If you encounter issues during extraction, re-download the dataset from Kaggle.

###Permission Issues:
Ensure you have set the correct permissions using chmod as shown above.

##7. Additional Resources

###Kaggle Dataset Page:
PACS Dataset on Kaggle

###Official PACS Dataset Documentation:
Refer to relevant research papers or the dataset documentation provided on Kaggle for more details.
