#!/usr/bin/env python3
# iris_nn_p4.py: classify Iris dataset using TensorFlow with cross-validation

import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import datetime
import io

# Load and prepare data
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# PCA visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(scaler.fit_transform(X))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(iris.target_names)
plt.show()

# Combine train and validation for cross-validation
X_train_full = X_train
y_train_full = y_train

# Define a learning rate schedule
def lr_schedule(epoch):
    initial_lr = 0.001
    return initial_lr / (1 + 0.05 * epoch)

# Custom callback to log validation confusion matrix
class ConfusionMatrixCallback(tf.keras.callbacks.Callback):
    def __init__(self, val_dataset, log_dir):
        super().__init__()
        self.val_dataset = val_dataset
        self.writer = tf.summary.create_file_writer(log_dir + "/validation_cm")

    def on_epoch_end(self, epoch, logs=None):
        val_data, val_labels = next(iter(self.val_dataset.unbatch().batch(len(val_labels))))
        val_pred = np.argmax(self.model.predict(val_data, verbose=0), axis=1)
        cm = confusion_matrix(val_labels, val_pred)
        with self.writer.as_default():
            tf.summary.image("Validation Confusion Matrix", plot_to_image(cm, epoch), step=epoch)

# Helper function to convert confusion matrix to TensorBoard image
def plot_to_image(cm, epoch):
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
    disp.plot(cmap='Blues', ax=ax)
    plt.title(f'Validation Confusion Matrix - Epoch {epoch}')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    image = tf.image.decode_png(buf.getvalue(), channels=4)
    image = tf.expand_dims(image, 0)
    return image

# Cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
test_accuracies = []
val_accuracies = []

for fold, (train_idx, val_idx) in enumerate(kf.split(X_train_full)):
    print(f"\nFold {fold+1}/5")
    X_tr, X_v = X_train_full[train_idx], X_train_full[val_idx]
    y_tr, y_v = y_train_full[train_idx], y_train_full[val_idx]

    # Create datasets
    train_dataset = tf.data.Dataset.from_tensor_slices((X_tr, y_tr)).shuffle(100).batch(32)
    val_dataset = tf.data.Dataset.from_tensor_slices((X_v, y_v)).batch(32)
    test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)

    # Build simpler model with Dropout
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(4,)),
        tf.keras.layers.Dense(32),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU(),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(16),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.ReLU(),
        tf.keras.layers.Dense(3, activation='softmax')
    ])

    # Compile model
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # Define callbacks
    log_dir = f"logs/fit/fold_{fold+1}_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
    cm_callback = ConfusionMatrixCallback(val_dataset, log_dir)
    early_stopping = tf.keras.callbacks.EarlyStopping(
        monitor='val_loss', patience=20, restore_best_weights=True
    )
    lr_scheduler = tf.keras.callbacks.LearningRateScheduler(lr_schedule)
    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        f'best_model_fold_{fold+1}.keras', monitor='val_loss', save_best_only=True, mode='min'
    )

    # Train model
    history = model.fit(train_dataset, epochs=100, validation_data=val_dataset,
                        callbacks=[early_stopping, lr_scheduler, checkpoint, tensorboard_callback, cm_callback], verbose=1)

    # Load best model
    model = tf.keras.models.load_model(f'best_model_fold_{fold+1}.keras')

    # Evaluate on validation and test sets
    val_loss, val_accuracy = model.evaluate(val_dataset, verbose=0)
    test_loss, test_accuracy = model.evaluate(test_dataset, verbose=0)
    print(f"Fold {fold+1} Validation Accuracy: {val_accuracy:.4f}")
    print(f"Fold {fold+1} Test Accuracy: {test_accuracy:.4f}")
    val_accuracies.append(val_accuracy)
    test_accuracies.append(test_accuracy)

    # Test confusion matrix for the last fold
    if fold == 4:
        test_data, test_labels = next(iter(test_dataset.unbatch().batch(len(y_test))))
        test_pred = np.argmax(model.predict(test_data, verbose=0), axis=1)
        cm = confusion_matrix(test_labels, test_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
        disp.plot(cmap='Blues')
        plt.title(f'Test Confusion Matrix - Fold {fold+1}')
        plt.show()

        # Analyze test misclassifications
        test_misclassified = np.where(test_labels != test_pred)[0]
        print("Misclassified test samples (index, true label, predicted label, features):")
        unscaled_test_data = scaler.inverse_transform(test_data.numpy())
        for idx in test_misclassified:
            print(f"Index: {idx}, True: {iris.target_names[test_labels[idx]]}, Predicted: {iris.target_names[test_pred[idx]]}, "
                  f"Scaled Features: {test_data[idx].numpy()}, Unscaled Features: {unscaled_test_data[idx]}")

# Print cross-validation results
print(f"\nMean Validation Accuracy: {np.mean(val_accuracies):.4f} ± {np.std(val_accuracies):.4f}")
print(f"Mean Test Accuracy: {np.mean(test_accuracies):.4f} ± {np.std(test_accuracies):.4f}")

# Print class means
X_unscaled = scaler.inverse_transform(X_train)
for cls in range(3):
    cls_mask = y_train == cls
    print(f"{iris.target_names[cls]} mean features: {np.mean(X_unscaled[cls_mask], axis=0)}")

# Plot training and validation accuracy/loss for the last fold
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Accuracy over Epochs (Last Fold)')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss over Epochs (Last Fold)')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()

# Plot learning rate for the last fold
plt.figure(figsize=(6, 4))
lr_rates = [lr_schedule(epoch) for epoch in range(len(history.history['loss']))]
plt.plot(lr_rates, label='Learning Rate')
plt.title('Learning Rate over Epochs (Last Fold)')
plt.xlabel('Epoch')
plt.ylabel('Learning Rate')
plt.legend()
plt.show()
