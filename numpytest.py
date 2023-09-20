import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)

res = np.dot(a, b)
print(res)

# lists some activiation functions
# def relu(x):
def relu(x):
    return np.maximum(0, x)

print('relu(0.5)', relu(0.5))

# def tanh(x):
def tanh(x):
    return np.tanh(x)

print('tanh(0.5)', tanh(0.5))

# def sigmoid(x):
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

print('sigmoid(0.5)', sigmoid(0.5))
