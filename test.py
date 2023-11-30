import numpy as np
import tensorflow as tf
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelBinarizer

def test(data, labels):
    # Load best model
    best_model = tf.keras.models.load_model('best_model_resnet.h5')

    # Reshape the data
    X_test = data.T.reshape(-1, 300, 300, 3)

    # Label encoding
    lb = LabelBinarizer()
    y_test = lb.fit_transform(labels)

    # Predictions
    predictions = best_model.predict(X_test)
    predicted_labels = np.argmax(predictions, axis=1)

    # Calculate accuracy
    accuracy = accuracy_score(np.argmax(y_test, axis=1), predicted_labels)

    return accuracy, predicted_labels