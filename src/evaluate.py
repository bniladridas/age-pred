import os
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error

def evaluate_model(model_path, data_dir):
    """Evaluates the trained model on the test set."""

    # Load the trained model
    model = tf.keras.models.load_model(model_path, compile=False)  # Load without compiling

    # Compile the model manually
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])  # Or your original optimizer

    # Load test data
    X_test = np.load(os.path.join(data_dir, 'X_test.npy'))
    y_test = np.load(os.path.join(data_dir, 'y_test.npy'))

    # Evaluate the model
    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Mean Absolute Error: {mae:.2f}")

if __name__ == "__main__":
    model_path = "saved_models/age_prediction_model.h5"
    data_directory = "data/processed"
    evaluate_model(model_path, data_directory)