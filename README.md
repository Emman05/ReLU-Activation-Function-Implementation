# ReLU Activation Function Implementation

This project demonstrates the implementation of the **Rectified Linear Unit (ReLU)** activation function in Python. It includes an interactive web-based application built using Flask, along with usage examples, test cases, and a detailed explanation of the ReLU function's significance in neural networks.

## Features
- **Interactive Web App**: Users can input numerical data to apply the ReLU function and view the results.
- **ReLU Implementation**: Includes a Python implementation of the ReLU function.
- **Significance of ReLU**: Documentation explaining why ReLU is important in the context of neural networks.
- **Test Cases**: A Python script to test the ReLU function.
- **Example Usage**: Provides examples of ReLU usage in machine learning contexts.

---

## Table of Contents
1. [Introduction to ReLU](#introduction-to-relu)
2. [Significance of ReLU in Neural Networks](#significance-of-relu-in-neural-networks)
3. [How to Run the Project](#how-to-run-the-project)
4. [Input and Output Examples](#input-and-output-examples)
5. [Project Structure](#project-structure)
6. [Test Cases](#test-cases)

---

## Introduction to ReLU
The Rectified Linear Unit (ReLU) is a popular activation function in neural networks. The function is mathematically defined as:

\[ f(x) = \max(0, x) \]

This means that for any input greater than or equal to 0, ReLU returns the input value itself. For negative inputs, it returns 0.

---

## Significance of ReLU in Neural Networks
1. **Non-Linearity**: ReLU introduces non-linearity into the neural network, enabling it to learn complex patterns.
2. **Efficient Computation**: ReLU is computationally simple and fast compared to other activation functions like sigmoid and tanh.
3. **Mitigates Vanishing Gradients**: By not saturating for large positive values, ReLU avoids the vanishing gradient problem, which can hinder model training.
4. **Widely Used**: ReLU is the most commonly used activation function in deep learning models due to its performance advantages.

---

## How to Run the Project
### Prerequisites
- Python 3.7+
- Flask

### Setup
1. Clone the repository or download the source code.
2. Install dependencies using pip:
   ```bash
   pip install flask
   ```
3. Navigate to the project directory and run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Input and Output Examples
### Example Input:
- Input: `12, 11, 13, -77, 98, -77`

### Output:
- ReLU Output: `12, 11, 13, 0, 98, 0`

---

## Project Structure
```
project_directory/
|
├── app.py                 # Main Flask application
├── templates/             # HTML files for the web interface
│   ├── index.html         # Input page
│   └── result.html        # Result page
├── static/                # CSS files for styling
│   ├── style.css          # Styling for index.html
│   └── result.css         # Styling for result.html
└── tests.py               # Unit tests for the ReLU function
```

---

## Test Cases
A set of test cases has been provided in the `tests.py` file to ensure the correctness of the ReLU implementation.

### Example Test Case:
```python
import unittest
from app import relu

class TestReLU(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(relu([1, 2, 3]), [1, 2, 3])

    def test_negative_values(self):
        self.assertEqual(relu([-1, -2, -3]), [0, 0, 0])

    def test_mixed_values(self):
        self.assertEqual(relu([-1, 2, -3, 4]), [0, 2, 0, 4])

    def test_single_value(self):
        self.assertEqual(relu(5), 5)
        self.assertEqual(relu(-5), 0)

if __name__ == '__main__':
    unittest.main()
```

Run the tests:
```bash
python tests.py
```


