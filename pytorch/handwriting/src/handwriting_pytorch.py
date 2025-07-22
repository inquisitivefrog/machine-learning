#!/usr/bin/env python3
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import joblib
from sklearn.preprocessing import StandardScaler
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("output/handwriting_pytorch.log"),
        logging.StreamHandler()
    ]
)

# Define model
class DigitClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.layers = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )
    def forward(self, x):
        x = self.flatten(x)
        return self.layers(x)

def train_model():
    # Load data
    transform = transforms.Compose([transforms.ToTensor()])
    train_dataset = datasets.Digits(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.Digits(root='./data', train=False, download=True, transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    # Initialize model
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    model = DigitClassifier().to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()

    # Train
    model.train()
    for epoch in range(10):
        total_loss = 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        logging.info(f"Epoch {epoch+1}, Loss: {total_loss/len(train_loader):.4f}")

    # Save model
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    torch.save(model.state_dict(), f"output/handwriting_pytorch_model_{timestamp}.pth")
    logging.info("Model saved")

    # Save scaler (for API compatibility)
    scaler = StandardScaler()
    X_train = train_dataset.data.reshape(-1, 64).numpy()
    scaler.fit(X_train)
    joblib.dump(scaler, "output/scaler.pkl")
    logging.info("Scaler saved")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    train_model()
