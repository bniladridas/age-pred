import os
import tensorflow as tf
from model import create_model
import numpy as np

def train_model(data_dir, model_save_path, epochs=20, batch_size=32):
    """Trains the age prediction model."""

    # Load processed data
    X_train = np.load(os.path.join(data_dir, 'X_train.npy'))
    y_train = np.load(os.path.join(data_dir, 'y_train.npy'))

    # Create the model
    model = create_model()
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Train the model
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    # Save the trained model
    model.save(model_save_path)

    print(f"Model saved to: {model_save_path}")

if __name__ == "__main__":
    processed_data_dir = "data/processed"
    model_save_path = "saved_models/age_prediction_model.h5"
    train_model(processed_data_dir, model_save_path)