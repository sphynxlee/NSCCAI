import cv2
import numpy as np

# Read image
src = cv2.imread('iron-puzzle.png', cv2.IMREAD_UNCHANGED)
print(src.shape)

# Set blue and green channels to zero
# src[:, :, :2] = np.zeros([src.shape[0], src.shape[1], 2])
src[:, :, 0] = 0
src[:, :, 1] = 0


# Enhance the red channel by multiplying it by 10
src[:, :, 2] = src[:,:,2] * 10

# Save image
cv2.imwrite('iron-solution.png', src)


