import cv2
import numpy as np

# Read image
src = cv2.imread('copper-puzzle.png', cv2.IMREAD_UNCHANGED)
print(src.shape)

# Set red channel to zero
src[:, :, 2] = 0

#enhance the blue and green BGR
src[:,:,0] = src[:,:,0] * 10
src[:,:,1] = src[:,:,1] * 10


# Enhance the red channel by multiplying it by 10

# Save image
cv2.imwrite('copper-solution.png', src)


