#!/usr/bin/env python3
# tensor_nn_batch.py: PyTorch example using torch.nn for noisy cos(x)/sin(x) regression, MNIST, or CIFAR-10 classification with batch training and validation
# No GPU required; runs on CPU
# ML workflow split into functions:
# 1. Forward pass (via nn.Module)
# 2. Loss computation
# 3. Backward pass
# 4. Weight updates
# 5. Visualize
# 6. Save model
# Adapted from https://pytorch.org/tutorials/beginner/pytorch_with_examples.html

import argparse
import datetime
import math
import psutil
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

class Net(nn.Module):
    """Neural network for noisy cos(x)/sin(x) regression."""
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, 128)
        self.bn1 = nn.BatchNorm1d(128)
        self.dropout1 = nn.Dropout(0.2)
        self.fc2 = nn.Linear(128, 128)
        self.bn2 = nn.BatchNorm1d(128)
        self.dropout2 = nn.Dropout(0.2)
        self.fc3 = nn.Linear(128, 1)
    
    def forward(self, x):
        x = torch.relu(self.bn1(self.fc1(x)))
        x = self.dropout1(x)
        x = torch.relu(self.bn2(self.fc2(x)))
        x = self.dropout2(x)
        x = self.fc3(x)
        return x

class MNISTNet(nn.Module):
    """Convolutional neural network for MNIST classification."""
    def __init__(self):
        super(MNISTNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 128, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(128)
        self.fc1 = nn.Linear(128 * 7 * 7, 256)
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(256, 10)
    
    def forward(self, x):
        x = torch.relu(self.bn1(self.conv1(x)))
        x = torch.max_pool2d(x, 2)
        x = torch.relu(self.bn2(self.conv2(x)))
        x = torch.max_pool2d(x, 2)
        x = x.view(-1, 128 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

class CIFAR10Net(nn.Module):
    """Convolutional neural network for CIFAR-10 classification."""
    def __init__(self):
        super(CIFAR10Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.conv2 = nn.Conv2d(64, 128, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(128)
        self.fc1 = nn.Linear(128 * 8 * 8, 256)  # After two pooling: 32→16→8
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(256, 10)
    
    def forward(self, x):
        x = torch.relu(self.bn1(self.conv1(x)))
        x = torch.max_pool2d(x, 2)
        x = torch.relu(self.bn2(self.conv2(x)))
        x = torch.max_pool2d(x, 2)
        x = x.view(-1, 128 * 8 * 8)
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

def compute_loss(y_pred, y, criterion, task):
    """Compute loss: MSE for regression, CrossEntropy for classification."""
    return criterion(y_pred, y if task in ['mnist', 'cifar10'] else y)

def compute_accuracy(y_pred, y):
    """Compute accuracy for classification."""
    _, predicted = torch.max(y_pred, 1)
    correct = (predicted == y).float().sum()
    return correct / y.shape[0]

def backward_pass(loss, model):
    """Compute gradients with autograd and clip gradients."""
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

def update_weights(optimizer):
    """Update weights using optimizer."""
    optimizer.step()
    optimizer.zero_grad()

def visualize(x, y, y_pred, xLabel, yLabel, task):
    """Plot true vs. predicted for regression or sample images for classification."""
    if task in ['mnist', 'cifar10']:
        fig, axes = plt.subplots(2, 5, figsize=(10, 4))
        y_pred = torch.argmax(y_pred, dim=1)
        for i, ax in enumerate(axes.flatten()):
            img = x[i].permute(1, 2, 0).numpy() if task == 'cifar10' else x[i].squeeze().numpy()
            if task == 'cifar10':
                img = img * 0.5 + 0.5  # Denormalize
                img = img.clip(0, 1)
            ax.imshow(img, cmap='gray' if task == 'mnist' else None)
            ax.set_title(f'Pred: {y_pred[i].item()}, True: {y[i].item()}')
            ax.axis('off')
        plt.tight_layout()
        plt.show()
    else:
        plt.plot(x.numpy(), y.numpy(), label=xLabel, color='blue')
        plt.plot(x.numpy(), y_pred.detach().numpy(), label=yLabel, color='red', linestyle='--')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'{xLabel} to {yLabel}')
        plt.show()

def ran(graph):
    # Set data type and device
    dtype = torch.float
    device = torch.device("cpu")
    print(f"Using {device} device")

    # Task-specific setup
    task = graph
    train_losses, val_losses = [], []
    if task in ['cos', 'sin']:
        # Create input tensor x (from -π to π, 2000 points) and output tensor y
        x = torch.linspace(-math.pi, math.pi, 2000, dtype=dtype, device=device).reshape(-1, 1)
        x_test = torch.linspace(-4, 4, 500, dtype=dtype, device=device).reshape(-1, 1)
        if graph == 'cos':
            y = torch.cos(x) + 0.03 * torch.randn_like(x)
            y_test = torch.cos(x_test)
        elif graph == 'sin':
            y = torch.sin(x) + 0.03 * torch.randn_like(x)
            y_test = torch.sin(x_test)
        
        # Create dataset and split into train/validation
        dataset = TensorDataset(x, y)
        train_size = int(0.8 * len(dataset))
        val_size = len(dataset) - train_size
        train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
        train_loader = DataLoader(train_dataset, batch_size=1024, shuffle=True, num_workers=2)
        val_loader = DataLoader(val_dataset, batch_size=1024, num_workers=2)
        
        # Initialize model, loss function, and optimizer
        model = Net().to(device)
        criterion = nn.MSELoss(reduction='sum')
        optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9, weight_decay=1e-4)
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)
        
        # Training parameters
        num_epochs = 50
        patience = 10
        loss_threshold = 0.5
        model_file = 'best_model.pth'
        final_model_file = 'tensor_nn_model.pth'
        log_interval = 25
        val_interval = 40
    else:
        # Load MNIST or CIFAR-10 dataset with error handling
        try:
            if task == 'mnist':
                transform = transforms.Compose([
                    transforms.ToTensor(),
                    transforms.Normalize((0.1307,), (0.3081,))
                ])
                train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
                model = MNISTNet().to(device)
            else:  # cifar10
                transform = transforms.Compose([
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomCrop(32, padding=4),
                    transforms.RandomRotation(10),
                    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
                    transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                ])
                train_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
                model = CIFAR10Net().to(device)
        except Exception as e:
            print(f"Error downloading {task.upper()}: {e}")
            return
        train_size = int(0.8 * len(train_dataset))
        val_size = len(train_dataset) - train_size
        train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True, num_workers=0)
        val_loader = DataLoader(val_dataset, batch_size=128, num_workers=0)
        
        # Initialize loss function and optimizer
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
        
        # Training parameters
        num_epochs = 20
        scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=num_epochs)
        patience = 10
        loss_threshold = 0.8
        model_file = f'best_{task}_model.pth'
        final_model_file = f'{task}_model.pth'
        log_interval = 50
        val_interval = 3

    # Training loop with early stopping
    best_val_loss = float('inf')
    patience_counter = 0
    total_iterations = 0
    for epoch in range(num_epochs):
        model.train()
        epoch_train_loss = 0
        for batch_x, batch_y in train_loader:
            total_iterations += 1
            y_pred = model(batch_x)
            loss = compute_loss(y_pred, batch_y, criterion, task)
            epoch_train_loss += loss.item()
            backward_pass(loss, model)
            update_weights(optimizer)
            if total_iterations % log_interval == 0:
                print(f"Iteration {total_iterations}, Batch Loss: {loss.item()}")
        train_losses.append(epoch_train_loss / len(train_loader))
        scheduler.step()

        # Compute validation loss and accuracy (for classification)
        model.eval()
        val_loss = 0
        val_accuracy = 0
        with torch.no_grad():
            for val_x, val_y in val_loader:
                val_pred = model(val_x)
                val_loss += compute_loss(val_pred, val_y, criterion, task).item()
                if task in ['mnist', 'cifar10']:
                    val_accuracy += compute_accuracy(val_pred, val_y).item()
        val_loss /= len(val_loader)
        val_losses.append(val_loss)
        val_accuracy = val_accuracy / len(val_loader) if task in ['mnist', 'cifar10'] else None
        model.train()
        
        # Log validation metrics
        if epoch % val_interval == 0 or epoch == num_epochs - 1:
            print(f"Epoch {epoch+1}, Validation Loss: {val_loss:.6f}" + 
                  (f", Validation Accuracy: {val_accuracy:.4f}" if task in ['mnist', 'cifar10'] else ""))
        
        # Log memory usage
        #print(f"Memory usage: {psutil.virtual_memory().percent}%")
        #print(f"Swap usage: {psutil.swap_memory().percent}%")
        
        # Early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            torch.save(model.state_dict(), model_file)
        else:
            patience_counter += 1
        if patience_counter >= patience or val_loss < loss_threshold:
            print(f"Early stopping at epoch {epoch+1}")
            break

    # Plot loss curves
    plt.plot(train_losses, label='Train Loss')
    plt.plot(val_losses, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title(f'{task.upper()} Loss Curve')
    plt.legend()
    plt.show()

    # Load best model
    model.load_state_dict(torch.load(model_file))

    # Compute final metrics and visualize
    model.eval()
    with torch.no_grad():
        if task in ['cos', 'sin']:
            full_y_pred = model(x)
            full_loss = compute_loss(full_y_pred, y, criterion, task)
            y_test_pred = model(x_test)
            print(f"Final Full-Dataset Loss: {full_loss.item()}")
            visualize(x.squeeze(), y, full_y_pred, xLabel=f'Noisy {graph}(x)', yLabel='Neural Network Fit', task=task)
            visualize(x_test.squeeze(), y_test, y_test_pred, xLabel=f'{graph}(x) (Test)', yLabel='Neural Network Fit (Test)', task=task)
        else:
            # Visualize sample predictions
            sample_x, sample_y = next(iter(val_loader))
            sample_pred = model(sample_x)
            visualize(sample_x.cpu(), sample_y.cpu(), sample_pred.cpu(), xLabel=f'{task.upper()} Samples', yLabel='Predicted', task=task)

    # Save final model
    torch.save(model.state_dict(), final_model_file)

    # Test reloaded model
    model.load_state_dict(torch.load(final_model_file))
    model.eval()
    with torch.no_grad():
        if task in ['cos', 'sin']:
            reloaded_y_pred = model(x)
            print(f"Reloaded model max difference: {(full_y_pred - reloaded_y_pred).abs().max().item()}")
        else:
            # Compute final validation accuracy
            final_accuracy = 0
            with torch.no_grad():
                for val_x, val_y in val_loader:
                    val_pred = model(val_x)
                    final_accuracy += compute_accuracy(val_pred, val_y).item()
            final_accuracy /= len(val_loader)
            print(f"Reloaded model final validation accuracy: {final_accuracy:.4f}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run regression or classification')
    parser.add_argument('--graph', type=str, default='cos', choices=['cos', 'sin', 'mnist', 'cifar10'],
                        help='Task to run: cos, sin, mnist, or cifar10')
    args = parser.parse_args()
    
    start_time = datetime.datetime.now()
    ran(args.graph)
    end_time = datetime.datetime.now()
    print(f"Execution time: {end_time - start_time}")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")
    print(f"Swap usage: {psutil.swap_memory().percent}%")
    print(f"CPU usage: {psutil.cpu_percent()}%")
