import cv2, os
import matplotlib.pyplot as plt

pwd = os.getcwd() + '/NSCCAI/codes/opencv_practice/'
print(pwd)
url = pwd + 'my_seven.jpg'

# from pathlib import Path
# print(Path.cwd())
# print(Path(__file__).resolve())

img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
print(img.shape)
img_resized = cv2.resize(img, (28, 28))
img_resized = cv2.bitwise_not(img_resized)
# cv2.imshow('image', img_resized)
# cv2.waitKey(0)
plt.imshow(img_resized, cmap='gray')
plt.show()
url = pwd + 'my_seven_new.jpg'
cv2.imwrite(url, img_resized)

