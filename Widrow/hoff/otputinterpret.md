# AND Gate Perceptron using Widrow-Hoff (Delta) Learning Rule

This project implements a single-layer perceptron to learn the behavior of the AND logic gate using the **Widrow-Hoff (Delta) Rule**, also known as the **Least Mean Squares (LMS)** method.

## 📌 Objective

Train a linear model to approximate the output of an AND gate, using gradient descent to minimize the error between predicted and target values.

---

## 🧠 Learning Process

The perceptron is trained over **multiple epochs** using the following parameters:

- **Initial weights:** Random (e.g., [0.5, 0.5])
- **Initial bias:** 0.5
- **Learning rate (η):** 0.1
- **Activation Function:** Linear (no thresholding during training)

### ✏️ Update Rule (Delta Rule)

For each input pattern:

```math
output = (w · x) + b  
error = target - output  
w = w + η * error * x  
b = b + η * error
🧪 Training Data (AND Gate)
Input	Target
[0, 0]	0
[0, 1]	0
[1, 0]	0
[1, 1]	1
📈 Sample Training Log (Epoch 1 - Epoch 20)
Each epoch consists of:

Calculating the output for each input

Computing the error (target - output)

Updating weights and bias accordingly

Example:

text
Copy
Edit
Epoch 1
 Input: [0 0], Output: 0.5, Target: 0, Error: -0.5
 Input: [0 1], Output: 0.95, Target: 0, Error: -0.95
 Input: [1 0], Output: 0.86, Target: 0, Error: -0.86
 Input: [1 1], Output: 1.09, Target: 1, Error: -0.09
 Weights: [0.4056 0.3961], Bias: 0.26
--------------------------------------------------
Epoch 10
 Input: [0 0], Output: -0.08, Target: 0, Error: 0.08
 Input: [0 1], Output: 0.31, Target: 0, Error: -0.31
 Input: [1 0], Output: 0.31, Target: 0, Error: -0.31
 Input: [1 1], Output: 0.6, Target: 1, Error: 0.4
 Weights: [0.4199 0.3939], Bias: -0.1
--------------------------------------------------
Epoch 20
 Input: [0 0], Output: -0.18, Target: 0, Error: 0.18
 Input: [0 1], Output: 0.29, Target: 0, Error: -0.29
 Input: [1 0], Output: 0.29, Target: 0, Error: -0.29
 Input: [1 1], Output: 0.66, Target: 1, Error: 0.34
 Weights: [0.4879 0.4594], Bias: -0.19
--------------------------------------------------
✅ Result
After training:

Inputs like [0, 0], [0, 1], [1, 0] produce outputs close to 0

Input [1, 1] produces output close to 1

This successfully models the behavior of an AND gate.

📎 Notes
A step function (thresholding) can be applied post-training to convert outputs to binary classification.

This approach can be extended to OR, XOR (with hidden layers), and other logic gates.

📁 Files
perceptron.py – Python code to train the AND gate perceptron using Delta Rule

README.md – This documentation

👨‍💻 Author
Aavanish Koirala
aavanishk@gmail.com










