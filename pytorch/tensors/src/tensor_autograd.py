#!/usr/bin/env python3
# tensor_autograd.py: PyTorch example using autograd to fit a fourth-order polynomial to sin(x)
# No GPU required; runs on CPU
# ML workflow split into functions:
# 1. Forward pass
# 2. Loss computation
# 3. Backward pass
# 4. Weight updates
# https://pytorch.org/tutorials/beginner/pytorch_with_examples.html
# https://pytorch.org/docs/stable/torch.html

import datetime
import math
import psutil
import torch
import matplotlib.pyplot as plt

def forward_pass(x, a, b, c, d, e, f):
    """Compute predicted y using a fourth-order polynomial."""
    return a + b * x + c * x ** 2 + d * x ** 3 + e * x ** 4 + f * x ** 5

def compute_loss(y_pred, y):
    """Compute mean squared error loss."""
    return (y_pred - y).pow(2).sum()

def backward_pass(loss, parameters, max_norm=1.0):
    """Compute gradients with autograd and clip them."""
    loss.backward()
    torch.nn.utils.clip_grad_norm_(parameters, max_norm=max_norm)

def update_weights(parameters, learning_rate):
    """Update weights using gradient descent."""
    #optimizer.step()
    with torch.no_grad():
        for param in parameters:
            param -= learning_rate * param.grad
            param.grad = None  # Zero gradient

def visualize(x, y, y_pred, xLabel, yLabel):
    # Plot the results
    plt.plot(x.numpy(), y.numpy(), label=xLabel, color='blue')
    plt.plot(x.numpy(), y_pred.detach().numpy(), label=yLabel, color='red', linestyle='--')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{xLabel} to {yLabel}')
    plt.show()

def ran(graph):
    # Set data type and device (CPU since no GPU is available)
    dtype = torch.float
    device = torch.device("cpu")
    print(f"Using {device} device")

    # Create input tensor x (from -π to π, 2000 points) and output tensor y = sin(x)
    x = torch.linspace(-math.pi, math.pi, 2000, dtype=dtype, device=device)
    # Normalize x to [-1, 1] to reduce magnitude of higher-order terms
    x_normalized = x / math.pi
    if graph == 'cos':
        # Taylor Series: 1 - x^2/2 + x^4/24
        y = torch.cos(x)
    elif graph == 'sin':
        # Taylor Series: x - x^3/6 + x^5/120
        y = torch.sin(x)

    # Initialize random weights for a fourth-order polynomial: y = a + b*x + c*x^2 + d*x^3 + e*x^4
    # requires_grad=True enables autograd to track operations for gradient computation
    a = torch.randn((), dtype=dtype, device=device, requires_grad=True)
    b = torch.randn((), dtype=dtype, device=device, requires_grad=True)
    c = torch.randn((), dtype=dtype, device=device, requires_grad=True)
    d = torch.randn((), dtype=dtype, device=device, requires_grad=True)
    e = torch.randn((), dtype=dtype, device=device, requires_grad=True)
    f = torch.randn((), dtype=dtype, device=device, requires_grad=True)
    parameters = [a, b, c, d, e, f]

    learning_rate = 1e-6  # Adjusted for faster convergence with normalization
    for t in range(2000):
        # ML workflow
        # 1. Forward pass
        y_pred = forward_pass(x_normalized, a, b, c, d, e, f)

        # 2. Loss computation
        loss = compute_loss(y_pred, y)
        if t % 100 == 99:
            print(f"Iteration {t}, Loss: {loss.item()}")

        # 3. Backward pass
        backward_pass(loss, parameters, max_norm=1.0)

        # 4. Weight updates
        #optimizer = torch.optim.SGD(parameters, lr=1e-4, momentum=0.5)
        update_weights(parameters, learning_rate)

    # 5. Visualize
    if graph == 'sin':
        visualize(x, y, y_pred, xLabel='sin(x)', yLabel='Polynomial Fit')
    elif graph == 'sin':
        visualize(x, y, y_pred, xLabel='cos(x)', yLabel='Polynomial Fit')

    s1 = f'Result: y = {a.item():.2f} + {b.item():.2f}x + {c.item():.2f}x^2 '
    s2 = f'+ {d.item():.2f}x^3 + {e.item():.2f}x^4 + {f.item():.2f}x^5'
    print(s1 + s2)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    ran(graph='cos')
    end_time = datetime.datetime.now()
    print(f'Execution time: {end_time - start_time}')
    print(f'Memory usage: {psutil.virtual_memory().percent}%')
    print(f'CPU usage: {psutil.cpu_percent()}%')
