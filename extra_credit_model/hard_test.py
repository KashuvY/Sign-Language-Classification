import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelBinarizer

def test(data_test_file_path, labels_test_file_path):
    threshold = 0.7
    
    # load data
    data_test = np.load(data_test_file_path)
    labels_test = np.load(labels_test_file_path)
    
    # Load best model
    best_model = tf.keras.models.load_model('best_model_extra_credit.h5')

    # Reshape the data
    X_test = data_test.T.reshape(-1, 300, 300, 3)

    # Label encoding
    lb = LabelBinarizer()
    y_test = lb.fit_transform(labels_test)  # assumes we already have some images labeled as -1 (so we have 10 classes total)
    # Predictions
    predictions = best_model.predict(X_test)
  
    # Modify prediction logic to include "unknown" class
    predicted_labels = np.argmax(predictions, axis=1)
    confident_mask = np.max(predictions, axis=1) >= threshold
    predicted_labels[~confident_mask] = -1  # Assign -1 for "unknown" predictions

    # Adjust accuracy calculation to ignore unknown predictions
    mask = predicted_labels != -1
    accuracy = accuracy_score(np.argmax(y_test[mask], axis=1), predicted_labels[mask])

    return accuracy, predicted_labels
