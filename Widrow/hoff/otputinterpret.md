<h1>AND Gate Perceptron using Widrow-Hoff (Delta) Learning Rule</h1>

<p>This project implements a <strong>single-layer perceptron</strong> to learn the behavior of the <strong>AND logic gate</strong> using the <strong>Widrow-Hoff (Delta) Rule</strong>, also known as the <strong>Least Mean Squares (LMS)</strong> method.</p>

<hr>

<h2>📌 Objective</h2>

<p>Train a linear model to approximate the output of an AND gate, using <strong>gradient descent</strong> to minimize the error between predicted and actual target values.</p>

<hr>

<h2>🧠 Learning Process</h2>

<p>The perceptron is trained over multiple epochs with the following configuration:</p>

<ul>
    <li><strong>Initial Weights:</strong> Random (e.g., [0.5, 0.5])</li>
    <li><strong>Initial Bias:</strong> 0.5</li>
    <li><strong>Learning Rate (η):</strong> 0.1</li>
    <li><strong>Activation Function:</strong> Linear (no thresholding during training)</li>
</ul>

<h3>✏️ Delta Rule (Update Formula)</h3>
<pre><code>
For each input pattern:
    output = (w · x) + b
    error  = target - output
    w      = w + η * error * x
    b      = b + η * error
</code></pre>

<hr>

<h2>🧪 Training Data (AND Gate)</h2>

<table border="1">
    <tr>
        <th>Input</th>
        <th>Target</th>
    </tr>
    <tr>
        <td>[0, 0]</td>
        <td>0</td>
    </tr>
    <tr>
        <td>[0, 1]</td>
        <td>0</td>
    </tr>
    <tr>
        <td>[1, 0]</td>
        <td>0</td>
    </tr>
    <tr>
        <td>[1, 1]</td>
        <td>1</td>
    </tr>
</table>

<hr>

<h2>📈 Sample Training Log (Epochs 1 to 20)</h2>

<p>Each epoch performs:</p>
<ul>
    <li>Calculating output</li>
    <li>Computing error (<code>target - output</code>)</li>
    <li>Updating weights and bias</li>
</ul>

<h3>🔁 Epoch 1</h3>
<pre><code>
Input: [0 0], Output: 0.5, Target: 0, Error: -0.5  
Input: [0 1], Output: 0.95, Target: 0, Error: -0.95  
Input: [1 0], Output: 0.86, Target: 0, Error: -0.86  
Input: [1 1], Output: 1.09, Target: 1, Error: -0.09  
Weights: [0.4056 0.3961], Bias: 0.26
</code></pre>

<h3>🔁 Epoch 10</h3>
<pre><code>
Input: [0 0], Output: -0.08, Target: 0, Error: 0.08  
Input: [0 1], Output: 0.31, Target: 0, Error: -0.31  
Input: [1 0], Output: 0.31, Target: 0, Error: -0.31  
Input: [1 1], Output: 0.6, Target: 1, Error: 0.4  
Weights: [0.4199 0.3939], Bias: -0.1
</code></pre>

<h3>🔁 Epoch 20</h3>
<pre><code>
Input: [0 0], Output: -0.18, Target: 0, Error: 0.18  
Input: [0 1], Output: 0.29, Target: 0, Error: -0.29  
Input: [1 0], Output: 0.29, Target: 0, Error: -0.29  
Input: [1 1], Output: 0.66, Target: 1, Error: 0.34  
Weights: [0.4879 0.4594], Bias: -0.19
</code></pre>

<hr>

<h2>✅ Result</h2>

<p>After training:</p>
<ul>
    <li>Inputs like [0, 0], [0, 1], [1, 0] produce outputs close to 0</li>
    <li>Input [1, 1] produces output close to 1</li>
</ul>

<p>This successfully models the behavior of an AND gate.</p>

<hr>

<h2>📎 Notes</h2>
<ul>
    <li>A step function (thresholding) can be applied post-training to convert outputs to binary classification.</li>
    <li>This approach can be extended to OR, XOR (with hidden layers), and other logic gates.</li>
</ul>

<hr>

<h2>📁 Files</h2>
<ul>
    <li><code>perceptron.py</code> – Python code to train the AND gate perceptron using Delta Rule</li>
    <li><code>README.md</code> – This documentation</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p>Aavanish Koirala</p>
<p><a href="mailto:aavanishk@gmail.com">aavanishk@gmail.com</a></p>

