# 🐟 Multiclass Fish Image Classification

## 📌 Project Overview

This project focuses on **classifying fish species using Deep Learning (CNN + Transfer Learning)**.
It uses image data to predict fish categories and provides a **real-time prediction interface using Streamlit**.

---

## 🚀 Features

* ✅ Multiclass Fish Classification
* ✅ Transfer Learning (MobileNetV2)
* ✅ Data Augmentation for better accuracy
* ✅ Model Evaluation (Accuracy, Precision, Recall, F1-score)
* ✅ Streamlit Web App for real-time predictions
* ✅ Confidence score visualization

---

## 🧠 Technologies Used

* Python 🐍
* TensorFlow / Keras
* NumPy, Pandas
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
Fish_Classification_Project/
│
├── data/                         # Dataset (Fish images)
├── models/                       # Saved models (.h5)
│   └── mobilenet_trained_model.h5
│
├── src/
│   ├── train.py                 # Model training
│   ├── evaluate.py              # Model evaluation
│   ├── predict.py               # Single image prediction
│
├── app.py                       # Streamlit application
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

* Image dataset organized into folders by fish species
* Loaded using `ImageDataGenerator`
* Includes preprocessing:

  * Rescaling
  * Rotation
  * Zoom
  * Flipping

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/fish-classification.git
cd fish-classification
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 1️⃣ Train Model

```bash
python src/train.py
```

### 2️⃣ Evaluate Model

```bash
python src/evaluate.py
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 🌐 Streamlit App

The web app allows users to:

* Upload fish images
* Predict fish species
* View confidence scores

### 📸 App Preview

* Upload image
* Get prediction instantly

---

## 🔍 Model Details

* Base Model: **MobileNetV2**
* Input Size: 224x224
* Output Layer: Softmax (Multiclass classification)
* Loss Function: Categorical Crossentropy
* Optimizer: Adam

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 🧪 Example Output

```
Predicted Class: sea_bass  
Confidence: 0.92  
```

---

## 💡 Key Learnings

* Transfer Learning improves performance significantly
* Data augmentation helps prevent overfitting
* Deployment using Streamlit makes ML models user-friendly

---

## 🚀 Future Improvements

* 🔹 Add multiple pretrained models (ResNet, VGG16, EfficientNet)
* 🔹 Add Grad-CAM visualization
* 🔹 Improve UI/UX of Streamlit app
* 🔹 Deploy on cloud (AWS / Render / HuggingFace Spaces)

---

## 👨‍💻 Author

**Suraj**

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
