import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iterations=80):
    z = 0
    for i in range(max_iterations):
        z = z*z + c
        if abs(z) > 2:
            return i  # Returns the number of iterations
    return max_iterations  # If still bounded within the specified number of times, return the maximum number of times

def generate_mandelbrot(width, height, real_start, real_end, imaginary_start, imaginary_end):
    mandelbrot_set = np.zeros((width, height))

    for x in range(width):
        for y in range(height):
            real_part = real_start + (x / width) * (real_end - real_start)
            imaginary_part = imaginary_start + (y / height) * (imaginary_end - imaginary_start)
            c = complex(real_part, imaginary_part)
            mandelbrot_set[x, y] = mandelbrot(c)

    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set):
    plt.imshow(mandelbrot_set.T, cmap='magma', extent=[-2, 2, -2, 2])
    plt.xlabel("Real-Axis")
    plt.ylabel("Imaginary-Axis")
    plt.title('mandelbrot_set set for $z_{{new}} = z^{{{}}} + c$'.format(2))
    plt.show()

# Setting the image size and coordinate range
width, height = 600, 600
real_start, real_end = -2, 2
imaginary_start, imaginary_end = -2, 2

# Generating Mandelbrot Collection Data
mandelbrot_set = generate_mandelbrot(width, height, real_start, real_end, imaginary_start, imaginary_end)

# plot the Mandelbrot set
plot_mandelbrot(mandelbrot_set)
