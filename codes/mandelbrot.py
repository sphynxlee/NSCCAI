# def in_mandelbrot(c, max_iterations=100):
#     z = 0
#     for i in range(max_iterations):
#         z = z**2 + c
#         if abs(z) > 2:
#             return i  # Returns the number of iterations
#     return max_iterations  # If still bounded within the specified number of times, return the maximum number of times

# # 举例
# c = complex(0.355, 0.355)
# iterations = in_mandelbrot(c)
# if iterations == 100:
#     print(f"{c} Belonging to the Mandelbrot Collection")
# else:
#     print(f"{c} does not belong to the Mandelbrot set, the number of iterations：{iterations}")

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iterations=100):
    z = 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i  # Returns the number of iterations
    return max_iterations  # If still bounded within the specified number of times, return the maximum number of times

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

# Setting the image size and coordinate range
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2

# Generating Mandelbrot Collection Data
mandelbrot_set = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max)

# plot the Mandelbrot set
plot_mandelbrot(mandelbrot_set)
