# def in_mandelbrot(c, max_iterations=100):
#     z = 0
#     for i in range(max_iterations):
#         z = z**2 + c
#         if abs(z) > 2:
#             return i  # 返回迭代次数
#     return max_iterations  # 如果在规定次数内仍然有界，返回最大次数

# # 举例
# c = complex(0.355, 0.355)
# iterations = in_mandelbrot(c)
# if iterations == 100:
#     print(f"{c} 属于曼德博集合")
# else:
#     print(f"{c} 不属于曼德博集合，迭代次数：{iterations}")

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iterations=100):
    z = 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i  # 返回迭代次数
    return max_iterations  # 如果在规定次数内仍然有界，返回最大次数

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max):
    mandelbrot_set = np.zeros((width, height))

    for x in range(width):
        for y in range(height):
            real_part = x * (x_max - x_min) / (width - 1) + x_min
            imaginary_part = y * (y_max - y_min) / (height - 1) + y_min
            c = complex(real_part, imaginary_part)
            mandelbrot_set[x, y] = mandelbrot(c)

    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set):
    plt.imshow(mandelbrot_set, cmap='hot', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title('Mandelbrot Set')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

# 设定图像大小和坐标范围
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2

# 生成曼德博集合数据
mandelbrot_set = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max)

# 绘制曼德博集合图形
plot_mandelbrot(mandelbrot_set)
