import cv2
import numpy as np

# Read image
src = cv2.imread('west-puzzle.png', cv2.IMREAD_UNCHANGED)
print(src.shape)

# Set red and green channels to zero
src[:, :, 2] = 0
src[:, :, 1] = 0


# drop >= 16 and multiple < 16 by 16
src[:, :, 0][src[:, :, 0] >= 16] = 0
src[:, :, 0][src[:, :, 0] < 16] *= 16

# move to blue channel to red channel BGR
src[:, :, 2] = src[:, :, 0]



# Save image
cv2.imwrite('west-solution.png', src)


