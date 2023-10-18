import torch
from tqdm import tqdm
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import pyNetwork

import os
pwd = os.getcwd()
print('pwd is: ', pwd)
# pwd = pwd + '/pyTeen.pth'
pwd = pwd + '/pyTeen-laura.pth'

# evaluation / testing loop

my_transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda img: img.view(784))])
testing_data = datasets.MNIST(root="data",train = False, download = True, transform = my_transform)

BATCH_SIZE = 16
testing_data_loader = DataLoader(testing_data, batch_size=BATCH_SIZE, shuffle=False)

pyTeen = pyNetwork.PyTeen()
pyTeen.load_state_dict(torch.load(pwd))

num_correct = 0
for input, label in tqdm(testing_data_loader):
    # print(f'input: {input.shape}')
    # print(f'label: {label.shape}')
    pred = pyTeen.predict(input)

    num_correct += (pred == label).sum()    # sum up all the correct predictions

print(f'num_correct: {num_correct}')
accuracy = (num_correct / len(testing_data_loader) * BATCH_SIZE).item()
print(f'accuracy: {accuracy}')
