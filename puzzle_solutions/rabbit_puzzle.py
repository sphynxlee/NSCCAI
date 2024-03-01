import cv2
import numpy as np

# Read image
src = cv2.imread('rabbit-puzzle.png', cv2.IMREAD_UNCHANGED)
print(src.shape)

# Set red and green channels to zero
src[:, :, 2] = 0
src[:, :, 1] = 0


# drop >= 16 and multiple < 16 by 16
# src[:, :, 0][src[:, :, 0] >= 16] = 0
# src[:, :, 0][src[:, :, 0] < 16] *= 16

# move to blue channel to red channel BGR
# src[:, :, 2] = src[:, :, 0]

# Enhance the blue channel by multiplying it by 10
src[:, :, 0] = src[:,:,0] * 10

# Save image
cv2.imwrite('rabbit-solution.png', src)


