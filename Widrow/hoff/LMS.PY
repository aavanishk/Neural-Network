import numpy as np

# Input features (AND logic gate)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target outputs
T = np.array([0, 0, 0, 1])

# Initialize weights and bias
weights = np.array([0.5, 0.5])
bias = 0.5

# Hyperparameters
learning_rate = 0.1
epochs = 20

# Training loop
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}")
    for i in range(len(X)):
        x = X[i]
        target = T[i]

        # Linear output (no step function!)
        output = np.dot(weights, x) + bias

        # Error (difference between target and output)
        error = target - output

        # Update weights and bias (Widrow-Hoff / LMS Rule)
        weights += learning_rate * error * x
        bias += learning_rate * error

        print(f" Input: {x}, Output: {round(output, 2)}, Target: {target}, Error: {round(error, 2)}")

    print(f" Weights: {weights}, Bias: {round(bias, 2)}")
    print("-" * 50)
