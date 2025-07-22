
(py3ml) tim@Tims-MBP tensorflow % vi mnist_cnn.py 
(py3ml) tim@Tims-MBP tensorflow % cat mnist_cnn.py 
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
(py3ml) tim@Tims-MBP tensorflow % ./mnist_cnn.py 
2025-05-09 14:30:34.968011: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Epoch 1/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 53s 34ms/step - accuracy: 0.8161 - loss: 0.5998 - val_accuracy: 0.9767 - val_loss: 0.0820 - learning_rate: 0.0010
Epoch 2/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9518 - loss: 0.1609 - val_accuracy: 0.9827 - val_loss: 0.0613 - learning_rate: 9.5238e-04
Epoch 3/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 45s 30ms/step - accuracy: 0.9629 - loss: 0.1298 - val_accuracy: 0.9869 - val_loss: 0.0498 - learning_rate: 9.0909e-04
Epoch 4/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9679 - loss: 0.1128 - val_accuracy: 0.9872 - val_loss: 0.0444 - learning_rate: 8.6957e-04
Epoch 5/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 30ms/step - accuracy: 0.9732 - loss: 0.0947 - val_accuracy: 0.9890 - val_loss: 0.0377 - learning_rate: 8.3333e-04
Epoch 6/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9772 - loss: 0.0815 - val_accuracy: 0.9902 - val_loss: 0.0394 - learning_rate: 8.0000e-04
Epoch 7/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9773 - loss: 0.0810 - val_accuracy: 0.9863 - val_loss: 0.0511 - learning_rate: 7.6923e-04
Epoch 8/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9784 - loss: 0.0751 - val_accuracy: 0.9900 - val_loss: 0.0458 - learning_rate: 7.4074e-04
Epoch 9/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9809 - loss: 0.0680 - val_accuracy: 0.9903 - val_loss: 0.0370 - learning_rate: 7.1429e-04
Epoch 10/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9822 - loss: 0.0626 - val_accuracy: 0.9893 - val_loss: 0.0474 - learning_rate: 6.8966e-04
Epoch 11/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9832 - loss: 0.0605 - val_accuracy: 0.9918 - val_loss: 0.0348 - learning_rate: 6.6667e-04
Epoch 12/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 48s 32ms/step - accuracy: 0.9849 - loss: 0.0578 - val_accuracy: 0.9918 - val_loss: 0.0331 - learning_rate: 6.4516e-04
Epoch 13/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9841 - loss: 0.0511 - val_accuracy: 0.9927 - val_loss: 0.0315 - learning_rate: 6.2500e-04
Epoch 14/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9863 - loss: 0.0470 - val_accuracy: 0.9912 - val_loss: 0.0324 - learning_rate: 6.0606e-04
Epoch 15/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9854 - loss: 0.0521 - val_accuracy: 0.9929 - val_loss: 0.0356 - learning_rate: 5.8824e-04
Epoch 16/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9855 - loss: 0.0485 - val_accuracy: 0.9945 - val_loss: 0.0305 - learning_rate: 5.7143e-04
Epoch 17/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9859 - loss: 0.0460 - val_accuracy: 0.9918 - val_loss: 0.0344 - learning_rate: 5.5556e-04
Epoch 18/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9855 - loss: 0.0531 - val_accuracy: 0.9933 - val_loss: 0.0305 - learning_rate: 5.4054e-04
Epoch 19/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9863 - loss: 0.0454 - val_accuracy: 0.9935 - val_loss: 0.0282 - learning_rate: 5.2632e-04
Epoch 20/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9883 - loss: 0.0430 - val_accuracy: 0.9937 - val_loss: 0.0291 - learning_rate: 5.1282e-04
Epoch 21/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 46s 31ms/step - accuracy: 0.9872 - loss: 0.0411 - val_accuracy: 0.9932 - val_loss: 0.0290 - learning_rate: 5.0000e-04
Epoch 22/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 47s 31ms/step - accuracy: 0.9883 - loss: 0.0405 - val_accuracy: 0.9942 - val_loss: 0.0279 - learning_rate: 4.8780e-04
Epoch 23/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 45s 30ms/step - accuracy: 0.9893 - loss: 0.0378 - val_accuracy: 0.9945 - val_loss: 0.0276 - learning_rate: 4.7619e-04
Epoch 24/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 45s 30ms/step - accuracy: 0.9892 - loss: 0.0374 - val_accuracy: 0.9954 - val_loss: 0.0236 - learning_rate: 4.6512e-04
Epoch 25/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 44s 29ms/step - accuracy: 0.9901 - loss: 0.0356 - val_accuracy: 0.9945 - val_loss: 0.0305 - learning_rate: 4.5455e-04
Epoch 26/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 45s 30ms/step - accuracy: 0.9896 - loss: 0.0354 - val_accuracy: 0.9938 - val_loss: 0.0294 - learning_rate: 4.4444e-04
Epoch 27/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 44s 29ms/step - accuracy: 0.9905 - loss: 0.0339 - val_accuracy: 0.9923 - val_loss: 0.0353 - learning_rate: 4.3478e-04
Epoch 28/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 45s 30ms/step - accuracy: 0.9899 - loss: 0.0356 - val_accuracy: 0.9938 - val_loss: 0.0277 - learning_rate: 4.2553e-04
Epoch 29/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 44s 29ms/step - accuracy: 0.9907 - loss: 0.0321 - val_accuracy: 0.9932 - val_loss: 0.0323 - learning_rate: 4.1667e-04
Epoch 30/30
1500/1500 ━━━━━━━━━━━━━━━━━━━━ 43s 29ms/step - accuracy: 0.9904 - loss: 0.0326 - val_accuracy: 0.9932 - val_loss: 0.0318 - learning_rate: 4.0816e-04

Test accuracy: 0.9938
Number of misclassified test samples: 62
Misclassified test samples (index, true label, predicted label):
Index: 320, True: 9, Predicted: 8
Index: 340, True: 5, Predicted: 3
Index: 542, True: 8, Predicted: 9
Index: 659, True: 2, Predicted: 1
Index: 674, True: 5, Predicted: 3
Number of misclassified validation samples: 55
Misclassified validation samples (index, true label, predicted label):
Index: 404, True: 4, Predicted: 9
Index: 614, True: 6, Predicted: 4
Index: 736, True: 0, Predicted: 8
Index: 763, True: 5, Predicted: 6
Index: 1021, True: 8, Predicted: 0
(py3ml) tim@Tims-MBP tensorflow %                 

