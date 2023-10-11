import torch
import numpy as np

# Directly from data
data = [[1,2,3],[4,5,6]]
x_data = torch.tensor(data)
print(f'x_data: {x_data}\n')

# From a NumPy array
np_array = np.array(data)
print(f'np_array: {np_array}\n')
x_np = torch.from_numpy(np_array)
print(f'x_np: {x_np}\n')

# From another tensor
x_ones = torch.ones_like(x_data) # retains the properties of x_data
print(f'x_ones: {x_ones}\n')

x_rand = torch.rand_like(x_data, dtype=torch.float) # overrides the datatype of x_data
print(f'x_rand: {x_rand}\n')

x_zeros = torch.zeros_like(x_data) # retains the properties of x_data
print(f'x_zeros: {x_zeros}\n')

# With random or constant values:
shape = (2,3)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
print(f'rand_tensor: {rand_tensor}\n')
print(f'ones_tensor: {ones_tensor}\n')
print(f'zeros_tensor: {zeros_tensor}\n')

# Attributes of a Tensor
tensor = torch.rand(3,4)
print(f'Shape of tensor: {tensor.shape}')
print(f'Datatype of tensor: {tensor.dtype}')
print(f'Device tensor is stored on: {tensor.device}')

# Operations on Tensors
# We move our tensor to the GPU if available
if torch.cuda.is_available():
    tensor = torch.tensor.to('cuda')
    print(f'Device tensor is stored on: {tensor.device}\n')
else:
    print('No GPU available, using CPU instead.\n')


# Standard numpy-like indexing and slicing
tensor = torch.ones(2,2)
tensor[1, 1] = 0
print(f'tensor: {tensor}\n')


# Joining tensors
t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(f't1: {t1}\n')


# Multiplying tensors
# This computes the element-wise product
print(f'tensor.mul(tensor): {tensor.mul(tensor)}\n')
# Alternative syntax:
print(f'tensor * tensor: {tensor * tensor}\n')


# This computes the matrix multiplication between two tensors
print(f'tensor.matmul(tensor.T): {tensor.matmul(tensor.T)}\n')
# Alternative syntax:
print(f'tensor @ tensor.T: {tensor @ tensor.T}\n')


# In-place operations Operations that have a _ suffix are in-place. For example: x.copy_(y), x.t_(), will change x.
print(f'tensor, before add 5: {tensor}\n')
tensor.add_(5)
print(f'tensor.add_(5): {tensor}\n')

tensor_new = torch.tensor([[2,3],[4,5]])
tensor.copy_(tensor_new)
print(f'tensor.copy_(tensor): {tensor}\n')
tensor_new.t_()
print(f'tensor_new.t_(): {tensor_new}\n')

# Bridge with NumPy

# Tensor to NumPy array
t = torch.ones(5)
print(f't: {t}\n')
n = t.numpy()
print(f'n: {n}\n')

# A change in the tensor reflects in the NumPy array.
t.add_(1)
print(f't.add_(1): {t}\n')
print(f'n: {n}\n')

# NumPy array to Tensor
n = np.ones(5)
print(f'n: {n}\n')
t = torch.from_numpy(n)
print(f't: {t}\n')

# Changes in the NumPy array reflects in the tensor.
np.add(n, 7, out=n)
print(f'np.add(n, 1, out=n): {n}\n')
print(f't: {t}\n')
