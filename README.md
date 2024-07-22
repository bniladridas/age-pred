# Age Prediction App

## Overview

This Streamlit application provides a user-friendly interface for predicting a person's age from an image. Simply upload an image, and the app will display the predicted age.

## Images

![data](/data/img/download.png)

## Features

- **Image Upload:** Upload images in common formats (JPEG, PNG).
- **Age Prediction:**  Uses a trained deep learning model to predict the age of the person in the image.
- **Real-time Results:** Get age predictions in real time, directly in your web browser. 

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://gitlab.com/niladridas/age-prediction-app.git
   cd age-prediction-app
   ```

2. **Create a Virtual Environment (Recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Train the Model (If you haven't already):**
   - Navigate to the `src` directory:  `cd src`
   - Run the training script: `python train.py`
   - The trained model will be saved to the `saved_models` directory.

2. **Run the Streamlit App:**
   ```bash
   streamlit run app/app.py 
   ```

3. **Access the App:**
   - Streamlit will start a development server. 
   - Open the provided local URL (usually `http://localhost:8501/`) in your web browser. 

## Project Structure

```
age-prediction-app/
  - app/           # Streamlit app code
    - app.py
  - data/          # Data directory (you may need to adjust paths)
    - raw/         # Raw image data (optional)
    - processed/   # Processed training/testing data
  - saved_models/  # Trained model files
  - src/           # Python scripts for training, etc.
    - train.py     # Model training script
    - ...
  - requirements.txt  # Project dependencies
  - README.md          # This file
```

## Dataset 

- **UTKFace:**  UTKFace dataset is a large-scale face dataset with long age span (range from 0 to 116 years old). The dataset consists of over 20,000 face images with annotations of age, gender, and ethnicity. The images cover large variation in pose, facial expression, illumination, occlusion, resolution, etc. This dataset could be used on a variety of tasks, e.g., face detection, age estimation, age progression/regression, landmark localization, etc. Some sample images are shown as following (e.g., A large-scale dataset of face images with labeled ages).
- **Source:** [Link to Dataset Website](https://susanqq.github.io/UTKFace/)

**Using Your Own Data:**
- **Format:** Images should be in `JPEG/PNG` format.
- **Directory Structure:** Create a `data` directory in the project root and organize your images into subfolders for training and testing.
- **Preprocessing:**  Ensure your images are preprocessed in the same way as the original training data. 

## Model 

This project uses a **Convolutional Neural Network (CNN)** for age prediction. 
- **Architecture:**  The model consists of multiple convolutional layers, each followed by a max-pooling layer. The output of the convolutional layers is then flattened and fed into a fully connected layer, which produces a single output representing the predicted age.
- **Loss Function:**   Mean Squared Error ('mse')
- **Optimizer:**  Adam

## Acknowledgements

- **Libraries:** This project leverages the following Python libraries:
    - TensorFlow
    - Keras
    - Streamlit
    - OpenCV
    - Pillow (PIL)

## License

- This is a project taken from [MIT License](/LICENSE).