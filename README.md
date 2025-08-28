
# Fish Species Classification
## Project Overview
This project aims to classify different species of fish using Deep Learning (Convolutional Neural Networks). It has two main components:

1. Model Training (FishImageClassification.ipynb)

A Jupyter Notebook for preprocessing data, building CNN models (and transfer learning), training, evaluating performance, and saving the best model.

2. Deployment App (FishIA.py)

A Streamlit-based web app where users can upload a fish image and get the predicted species with confidence scores.

## Project Structure

├── FishImageClassification.ipynb   # Model training, evaluation, and saving

├── FishIA.py                       # Streamlit app for prediction

├── data/                           # Dataset (train/test folders with fish images)

├── cnn_scratch_best.h5             # Trained CNN model (saved weights)

└── README.md                       # Project documentation

### Key Libraries

- Python 

- TensorFlow / Keras

- NumPy

- Matplotlib / Seaborn (for visualization)

- Streamlit (for deployment)
## Dataset
- Organized in train and test directories.

- Each class (fish species) has its own folder with respective images.

- Used ImageDataGenerator for data augmentation during training.
## Model Training
- Preprocess images (resize, normalize).

- Build a CNN model (trained from scratch / transfer learning).

- Train and validate on dataset.

- Evaluate with metrics: Accuracy, Loss, Confusion Matrix, etc.

- Save the best model as .h5.
## Features
- Upload an image (.jpg, .png, .jpeg).

- Model predicts the fish species.

- Displays confidence scores for each class.
## Example Usage
1. Run the Streamlit app.

2. Upload a fish image.

  - Get prediction:

    - ✅ Predicted species

    - 📊 Confidence distribution