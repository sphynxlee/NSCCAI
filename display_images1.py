import os
import struct
import numpy as np
import matplotlib.pyplot as plt

# Get the current working directory
pwd = os.getcwd()

# Path to the MNIST raw data file
data_file_path = os.path.join(pwd, 'data', 'MNIST', 'raw', 'train-images-idx3-ubyte')

# Open the data file in binary read mode
with open(data_file_path, 'rb') as data:
    # Read the header information
    magic_number, num_images, num_rows, num_cols = struct.unpack('>IIII', data.read(16))

    # Check the magic number to ensure it's the correct file type
    if magic_number != 2051:
        raise ValueError("This is not a MNIST image data file.")

    # Loop through the images
    for i in range(num_images):
        # Read pixel data for a single image (28x28 = 784 bytes)
        image_data = np.frombuffer(data.read(784), dtype=np.uint8)

        # Reshape the 1D array into a 2D image (28x28)
        image = image_data.reshape(28, 28)

        # Display the image using matplotlib
        plt.imshow(image, cmap='gray')
        plt.show()
