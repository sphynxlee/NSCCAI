# Applied SVD
# Goal: To read in an image into an array(PIL)
# Take that array(A) and decompose it into SVD
# drop some of the singular values (economy SVD)
# recreate the new (compressed) image array(A')
# save it and/or display it
# check out the compression ratio (file size)

# hints:
# we want a function like this: compress_image("doggie.jpg", k=10)
# U,S,Vt = np.linalg.svd()
# original_image = Image.open(image_path)
# original_matrix = np.array(original_image)
# suggest, start with grayscale [width, height, color_channels: grayscale]
# if (len(original_matrix.shape[2]) == 3): don't do this at first
# original_matrix = np.mean(original_matrix, axis=2)

# import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
pwd = os.getcwd()
pwd = pwd + "/NSCCAI/SVD/"

# function to compress image
def compress_image(image_src, num_svd):
    image_path = pwd + image_src

    # read in image
    original_image = Image.open(image_path)
    # convert to grayscale
    original_matrix = np.array(original_image)

    original_matrix = np.mean(original_matrix, axis=2)

    # check if image is color
    if (len(original_matrix.shape) == 3):
        original_matrix = np.mean(original_matrix, axis=2)


    # do SVD
    U, S, Vt = np.linalg.svd(original_matrix, full_matrices=False)
    # take out the k values
    Uk = U[:, :num_svd]
    Sk = S[:num_svd]
    Vtk = Vt[:num_svd, :]

    # reconstruct image
    compressed_matrix = Uk @ Sk @ Vtk

    # save image
    compressed_image = Image.fromarray(compressed_matrix.astype(np.uint8))
    compressed_image.save(f"{pwd}compressed_{num_svd}_{image_src}")
    # return compression ratio
    return (compressed_image.size[0] * compressed_image.size[1]) / (original_image.size[0] * original_image.size[1])

# function to plot images
def plot_image(image_path):
    # read in image
    original_image = Image.open(image_path)
    # convert to grayscale
    original_matrix = np.array(original_image)
    # check if image is color
    if (len(original_matrix.shape) == 3):
        original_matrix = np.mean(original_matrix, axis=2)
    # plot image
    plt.imshow(original_matrix, cmap='gray')
    plt.show()


image_src = "pug.jpg"
print(compress_image(image_src, 10))