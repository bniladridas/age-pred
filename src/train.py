# train.py 
import os
import numpy as np
import tensorflow as tf

def create_model():
    """Creates your age prediction model architecture."""
    # ... (Your model definition goes here) ...
    # Example (replace with your actual model):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(64, 64, 3)), # Assuming input images are 64x64 RGB
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # ... add more layers ...
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1) # Output layer for age regression
    ])
    return model

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

    # Save the trained model (use .keras format)
    model.save(model_save_path)
    print(f"Model saved to: {model_save_path}")

if __name__ == "__main__":
    processed_data_dir = "data/processed" 
    model_save_path = "saved_models/age_prediction_model.keras"
    train_model(processed_data_dir, model_save_path)