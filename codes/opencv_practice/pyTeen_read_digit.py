from torchvision import transforms
import pyNetwork
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os


pwd = os.getcwd() + '/NSCCAI/codes/opencv_practice/'
print(pwd)
url = pwd + 'dean-nine_new.jpg'

img = Image.open(url)
plt.imshow(img)
plt.show()

my_img_transform = transforms.Compose([transforms.Resize((28, 28)), transforms.ToTensor()])
input_img = my_img_transform(img).unsqueeze(0)


pyTeen = pyNetwork.PyTeen()
print(pyTeen.predict(input_img))
