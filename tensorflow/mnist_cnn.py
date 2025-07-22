#!/usr/bin/env python3
# mnist_cnn.py: classify handwritten digits using a CNN

import datetime
import io
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models

# Helper function for TensorBoard confusion matrix
def plot_to_image(cm, epoch):
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
    disp.plot(cmap='Blues', ax=ax)
    plt.title(f'Validation Confusion Matrix - Epoch {epoch}')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image = tf.image.decode_png(buf.getvalue(), channels=4)
    image = tf.expand_dims(image, 0)
    return image

# Custom callback to log validation confusion matrix
class ConfusionMatrixCallback(tf.keras.callbacks.Callback):
    def __init__(self, val_dataset, log_dir):
        super().__init__()
        self.val_dataset = val_dataset
        self.writer = tf.summary.create_file_writer(log_dir + "/validation_cm")

    def on_epoch_end(self, epoch, logs=None):
        val_data, val_labels = next(iter(self.val_dataset.unbatch().batch(len(y_val))))
        val_pred = np.argmax(self.model.predict(val_data, verbose=0), axis=1)
        cm = confusion_matrix(val_labels, val_pred)
        with self.writer.as_default():
            tf.summary.image("Validation Confusion Matrix", plot_to_image(cm, epoch), step=epoch)

# Load and preprocess MNIST data
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to [0, 1]
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Reshape for CNN (add channel dimension)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

# Split training data into training and validation sets
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

# Create TensorFlow datasets
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(48000).batch(32)
val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val)).batch(32)
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

# Define learning rate schedule
def lr_schedule(epoch):
    initial_lr = 0.001
    return initial_lr / (1 + 0.05 * epoch)

# Build CNN model with milder data augmentation and BatchNormalization
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.RandomRotation(0.05),
    layers.RandomZoom(0.05),
    layers.RandomTranslation(0.05, 0.05),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Define callbacks
log_dir = "logs/mnist/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
cm_callback = ConfusionMatrixCallback(val_dataset, log_dir)
lr_scheduler = tf.keras.callbacks.LearningRateScheduler(lr_schedule)

# Train the model
history = model.fit(train_dataset, epochs=30, validation_data=val_dataset,
                    callbacks=[early_stopping, tensorboard_callback, cm_callback, lr_scheduler], verbose=1)

# Evaluate the model
test_data, test_labels = next(iter(test_dataset.unbatch().batch(len(y_test))))
test_loss, test_accuracy = model.evaluate(test_dataset, verbose=0)
print(f"\nTest accuracy: {test_accuracy:.4f}")

# Generate predictions for test confusion matrix
y_pred = np.argmax(model.predict(test_data, verbose=0), axis=1)
cm = confusion_matrix(test_labels, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=range(10))
disp.plot(cmap='Blues')
plt.title('Test Confusion Matrix')
plt.show()

# Analyze misclassified test samples
misclassified = np.where(test_labels != y_pred)[0]
print(f"Number of misclassified test samples: {len(misclassified)}")
print("Misclassified test samples (index, true label, predicted label):")
for idx in misclassified[:5]:  # Limit to first 5
    print(f"Index: {idx}, True: {test_labels[idx]}, Predicted: {y_pred[idx]}")
    plt.imshow(test_data[idx].numpy().reshape(28, 28), cmap='gray')
    plt.title(f"True: {test_labels[idx]}, Predicted: {y_pred[idx]}")
    plt.show()

# Analyze misclassified validation samples
val_data, val_labels = next(iter(val_dataset.unbatch().batch(len(y_val))))
val_pred = np.argmax(model.predict(val_data, verbose=0), axis=1)
val_misclassified = np.where(val_labels != val_pred)[0]
print(f"Number of misclassified validation samples: {len(val_misclassified)}")
print("Misclassified validation samples (index, true label, predicted label):")
for idx in val_misclassified[:5]:  # Limit to first 5
    print(f"Index: {idx}, True: {val_labels[idx]}, Predicted: {val_pred[idx]}")
    plt.imshow(val_data[idx].numpy().reshape(28, 28), cmap='gray')
    plt.title(f"True: {val_labels[idx]}, Predicted: {val_pred[idx]}")
    plt.show()

# Plot training and validation accuracy/loss
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()
