import numpy as np
import matplotlib.pyplot as plt
import os
pwd = os.getcwd()
print(pwd)

image_url = pwd + '/data/MNIST/raw/' + 'train-images-idx3-ubyte'
image_data = open(image_url, 'rb')

label_url = pwd + '/data/MNIST/raw/' + 'train-labels-idx1-ubyte'
label_data = open(label_url, 'rb')

# print(data.read(4)) # magic number, means the file type
# also grab the label data....let you compare your ASCII art output with the label
# BONUS: use matplotlib to display the image and the label
# google: code page

image_data.read(16) # skip the header
label_data.read(8) # skip the header


# Hints:
# look in the ord() function
# output 28 bytes per line

# print(data.read(1)) # pixel value, read one BYTE then move the start of the next read one BYTE forward
# print(ord(data.read(1))) # pixel value, read one BYTE then move the start of the next read one BYTE forward

actual_number = ord(label_data.read(1))
print(f'actual_number = {actual_number}')
pixels = []
for i in range(28*28):  # this would be correct total # of bytes if there was no header
    current_character = ord(image_data.read(1))
    pixels.append(current_character)
    if current_character == 0:
        current_character = '0'
    else:
        current_character = '*'
    if i % 28 == 0:
        print('')
    print(current_character, end='')

pixels = np.array(pixels)
pixels = pixels.reshape(28, 28)
plt.imshow(pixels, cmap='gray')
plt.show()