import numpy as np

# 一维数组，点积和矩阵乘法相同
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = np.dot(a, b)
matrix_multiply = a @ b

print("Dot Product:", dot_product)
print("Matrix Multiply:", matrix_multiply)


import numpy as np
# 创建两个矩阵
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# 使用 @ 运算符进行矩阵乘法
C = A @ B
D = np.matmul(A, B)

print(C)
print(D)