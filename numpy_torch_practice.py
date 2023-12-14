import numpy as np

targets = np.zeros(5) + 0.01
print(targets)

targets2 = np.array(targets,ndmin=2).T
print(targets2)
# =============================================================================
import numpy as np
import torch

# Create a NumPy array
numpy_array = np.array([[1, 2, 3], [4, 5, 6]])
print(numpy_array)
# Convert NumPy array to PyTorch tensor
torch_tensor = torch.from_numpy(numpy_array)
print(torch_tensor)
# =============================================================================
import torch

# Create two matrices
matrix1 = torch.tensor([[1, 2], [3, 4]])
matrix2 = torch.tensor([[5, 6], [7, 8]])

# Matrix multiplication using torch.mm()
result = torch.mm(matrix1, matrix2)
print(result)
result2 = torch.mul(matrix1, matrix2)
print(result2)
# =============================================================================
import torch

# Create two matrices
matrix1 = torch.tensor([[1, 2], [3, 4]])
matrix2 = torch.tensor([[5, 6], [7, 8]])

# Matrix multiplication using the @ operator
result = matrix1 @ matrix2
print(result)
# =============================================================================
import torch

# Create a tensor with requires_grad set to True
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
print(f'x shape is: {x.shape}')

# Perform some operations
y = x.sum()
print(f'y is: {y}')
z0 = y * 2
z = z0 * 3
print(f'z is: {z}')

# The gradient of z with respect to x will be computed
z.backward()

# Access the gradients
print(f'x.grad is: {x.grad}')  # This will contain the gradient of z with respect to x
