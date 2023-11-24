import cv2, os
import matplotlib.pyplot as plt

pwd = os.getcwd() + '/NSCCAI/codes/opencv_practice2/west/'
pwd = pwd + 'west-puzzle.png'
print(pwd)

image = cv2.imread(pwd)

# BGR
image[:, :, 1] = 0  # green
image[:, :, 2] = 0  # red

import numpy as np
a = np.arange(6).reshape(2,3)
print(a[:,2])

# if a blue value is less than 16, set it to multiply 16
# if a blue value is greater than 16, set it to 0

# if image[:, :, 0] >= 16:
#     image[:, :, 0] = 0
# else:
#     image[:, :, 0] = image[:, :, 0] * 16

# # image[:, :, 2] = image[:, :, 0]

# plt.imshow(image)
# plt.show()