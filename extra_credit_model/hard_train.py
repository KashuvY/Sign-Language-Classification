import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Conv2D, MaxPooling2D, Flatten, Dense, Dropout,
                                     GlobalAveragePooling2D, BatchNormalization)
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.regularizers import l2


def train():
    # load data and labels
    data_train = np.load('data_train.npy').T
    labels_train = np.load('labels_train.npy')

    # Split and reshape the data
    train_df, test_df, train_df_labels, test_df_labels = train_test_split(data_train,
                                                                          labels_train,
                                                                          test_size=0.3,
                                                                          random_state=42
                                                                          )
    X_train = train_df.reshape(-1, 300, 300, 3)
    X_val = test_df.reshape(-1, 300, 300, 3)

    # Label encoding
    lb = LabelBinarizer()
    y_train = lb.fit_transform(np.concatenate([train_df_labels, [10]]))[:-1]  # Adds a dummy label for the 10th class and then removes it
    y_test = lb.transform(test_df_labels)

    # Model

    # initialize and activate base model of ResNet50
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(300, 300, 3))
    base_model.trainable = True

    # declare regularizer and model using base model
    regularizer = l2(1e-5)
    model = Sequential([base_model,
                        GlobalAveragePooling2D(),
                        Dense(1024, activation='relu', kernel_regularizer=regularizer),
                        BatchNormalization(),
                        Dropout(0.5),
                        Dense(10, activation='softmax', kernel_regularizer=regularizer)
    ])

    # Compiling model
    model.compile(optimizer=Nadam(learning_rate=1e-4), loss='categorical_crossentropy', metrics=['accuracy'])

    # Callbacks
    early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5)
    checkpoint = ModelCheckpoint('best_model_resnet.h5', monitor='val_loss', save_best_only=True)

    # Training
    model.fit(X_train, y_train, epochs=50, batch_size=16, validation_data=(X_val, y_val), callbacks=[early_stopping, reduce_lr, checkpoint])

    # Saving best model
    best_model = tf.keras.models.load_model('best_model_extra_credit.h5')

    if __name__ == "__main__":
        train()
