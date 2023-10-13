import torch

# t1 = torch.empty(1,2)
# t1 = torch.tensor([[1,2],[3,4]])
# print(f't1: {t1}\n')

# t2 = torch.rand(2,2)
# print(f't2: {t2}\n')

# t3 = torch.zeros(2,2)
# print(f't3: {t3}\n')

# t4 = torch.zeros_like(t1)
# print(f't4: {t4}\n')

# t5 = torch.ones(2,2)
# print(f't5: {t5}\n')

# t7 = torch.rand(2,2)
t7 = torch.tensor([[1,2],[3,4]])
print(f't7: {t7}\n')
# t8 = torch.rand(1,2)
t8 = torch.tensor([5,6])
print(f't8 shape is: {t8.shape}\n')
print(f't8: {t8}\n')
# c1 = t7 + t8
# print(f'c1: {c1}\n')
# c2 = torch.add(t7, t8)
# print(f'c2: {c2}\n')
# c3 = t7 - t8
# print(f'c3: {c3}\n')
c4 = t7 @ t8
print(f'c4: {c4}\n')



a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([[5,6],[7,8]])
# tensor multiplication
c = a * b
c = torch.mul(a, b)

# tensor dot product
c = a @ b
c = torch.matmul(a, b)

# tensor division
c = a / b
c = torch.div(a, b)
print(f'c: {c}\n')


a = torch.ones(5)
print(f'a: {a}\n')
print(f'a.dtype: {a.dtype}\n')
b = a.numpy()
print(f'b: {b}\n')
print(f'b.dtype: {b.dtype}\n')

a.add_(1)
print(f'a.add_(1): {a}\n')
print(f'b: {b}\n')

# tensor attributes
a = torch.rand(5,5)
print(f'a.shape: {a.shape}\n')
print(f'a.dtype: {a.dtype}\n')
print(f'a.device: {a.device}\n')
print(f'requires_grad: {a.requires_grad}\n')

import torch
# tensor slicing
a = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(f'a: {a}\n')
print(f'a\'s first row: {a[0]}\n')
print(f'a\'s first column: {a[:,0]}\n')
print(f'a\'s [3] element: {a[1,2].item()}\n')

# tensor reshaping
a = torch.rand(4,4)
print(f'a: {a}\n')
b = a.view(16)
print(f'b: {b}\n')
c = a.view(2, -1)
print(f'c: {c}\n')

a = torch.tensor([2, 2])
print(f'a: {a}\n')
b = torch.tensor([3, 3])
print(f'b: {b}\n')
I = torch.tensor([[1,0],[0,1]])
print(f'I: {I}\n')

print(f'a * I: {a * I}\n')
print(f'I * b: {I * b}\n')
print(f'a * I * b: {a * I * b}\n')