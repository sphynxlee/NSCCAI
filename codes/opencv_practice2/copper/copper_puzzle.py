import cv2, os
import matplotlib.pyplot as plt

pwd = os.getcwd() + '/NSCCAI/codes/opencv_practice2/copper/'
pwd = pwd + 'copper-puzzle.png'
print(pwd)

image = cv2.imread(pwd)
image[:, :, 2] = 0

# BGR, blue and green need to multiply 20
image[:, :, 0] = image[:, :, 0] * 20
image[:, :, 1] = image[:, :, 1] * 20

plt.imshow(image)
plt.show()