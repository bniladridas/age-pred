import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def load_data(data_dir, img_size=(64, 64)):
    """Loads and preprocesses images from the UTKFace dataset."""
    images = []
    ages = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".jpg"): 
            img_path = os.path.join(data_dir, filename)
            img = cv2.imread(img_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
            img = cv2.resize(img, img_size)
            images.append(img)

            age = int(filename.split("_")[0])
            ages.append(age)

    return np.array(images), np.array(ages)

def preprocess_and_save(data_dir, save_dir, img_size=(64, 64), test_size=0.2, random_state=42):
    """Loads, preprocesses, splits, and saves data."""
    images, ages = load_data(data_dir, img_size)

    # Normalize pixel values
    images = images / 255.0

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        images, ages, test_size=test_size, random_state=random_state
    )

    # Save processed data
    np.save(os.path.join(save_dir, 'X_train.npy'), X_train)
    np.save(os.path.join(save_dir, 'X_test.npy'), X_test)
    np.save(os.path.join(save_dir, 'y_train.npy'), y_train)
    np.save(os.path.join(save_dir, 'y_test.npy'), y_test)

if __name__ == "__main__":
    data_directory = "data/raw/UTKFace" 
    save_directory = "data/processed"
    preprocess_and_save(data_directory, save_directory)