import cv2, os
import matplotlib.pyplot as plt

pwd = os.getcwd() + '/NSCCAI/codes/opencv_practice2/iron_puzzle/'
pwd = pwd + 'iron-puzzle.png'
print(pwd)

image = cv2.imread(pwd)
# Notice: usually the color sequence is: RGB, but in openCV is BGR
img_copy = image.copy()

# S1: change bule and green to 0 to get noise out
img_copy[:, :, 0] = 0
img_copy[:, :, 1] = 0

# S2: multiply red by 10
img_copy[:, :, 2] = img_copy[:, :, 2] * 10
plt.imshow(img_copy)
plt.show()