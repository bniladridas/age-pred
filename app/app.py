import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

# --- Model Loading ---
# (Keep this part at the top)
@st.cache_resource  # Cache the loaded model for faster performance
def load_model(model_path):
    """Loads the trained Keras model."""
    model = load_model("../saved_models/age_prediction_model.keras") 
    return model

model = load_model("saved_models/age_prediction_model.keras") 

# --- Image Preprocessing ---
def preprocess_image(image, target_size=(64, 64)):
    """Preprocesses a single image for prediction."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image / 255.0  
    image = np.expand_dims(image, axis=0) 
    return image

# --- Streamlit App ---
st.title("Age Prediction App")

# --- File Uploader ---
uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

# --- Prediction and Display ---
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Make prediction
    try:
        preprocessed_image = preprocess_image(np.array(image))
        prediction = model.predict(preprocessed_image)
        predicted_age = int(prediction[0][0])
        st.write(f"Predicted Age: {predicted_age}")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")