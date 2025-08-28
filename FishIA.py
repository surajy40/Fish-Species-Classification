# Importing Important Libraries
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

#  Load your trained model
MODEL_PATH = "C:/Users/91886/Desktop/My Computer/Project_guvi/Fish Identfication Deep Learning/cnn_scratch_best.h5"  # update if saved as .h5
model = load_model(MODEL_PATH)

# Get class names from training data
# (Assumes you trained with ImageDataGenerator.flow_from_directory)
train_dir = "data/train"  # update path if different
class_names = sorted(os.listdir(train_dir))


st.title("🐟 Fish Species Classifier")
st.write("Upload a fish image, and the model will predict its category.")


uploaded_file = st.file_uploader("Choose a fish image...", type=["jpg", "png", "jpeg"])


def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # must match training input size
    img_array = image.img_to_array(img) / 255.0  # rescale [0,1]
    img_array = np.expand_dims(img_array, axis=0)  # add batch dimension

    preds = model.predict(img_array)[0]  # probability for each class
    predicted_class = class_names[np.argmax(preds)]
    confidence_scores = {class_names[i]: float(preds[i]) for i in range(len(class_names))}

    return predicted_class, confidence_scores

if uploaded_file is not None:
    # Save temp image
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())



    st.image("temp.jpg", caption="Uploaded Image", use_column_width=True)

    predicted_class, confidence_scores = predict_image("temp.jpg")

    st.subheader(f"✅ Prediction: {predicted_class}")
    st.write("### Confidence Scores:")
    st.json(confidence_scores)