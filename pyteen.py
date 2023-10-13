from torch import nn, optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# training_data = datasets.MNIST(root="data",train=True, download=True, transform=None)
# testing_data = datasets.MNIST(root="data",train=False, download=True, transform=None)
# print(f'training_data: {training_data[0]}\n')
# print(f'training_data: {training_data[0][0]}\n')
# plt.imshow(training_data[0][0])
# plt.show()

my_transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda img: img.view(784))])
training_data = datasets.MNIST(root="data",train = True, download = True, transform = my_transform)
testing_data = datasets.MNIST(root="data",train = False, download = True, transform = my_transform)
# print(f'training_data: {training_data[0][0].shape}\n')


class PyTeen (nn.Module):
    def __init__(self) -> None:
        super().__init__()
        # self.layers.append(nn.Linear(784, 128))
        self.layers = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )
        self.loss = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.parameters())

    # forward is a prediction
    def forward(self, input):
        return self.layers(input)

    # train is a loss
    # label is a actual value
    def train(self, input, label):
        self.optimizer.zero_grad()          # set gradients to zero
        prediction = self.forward(input)    # do the prediction on the input
        # loss = prediction - label
        loss = self.loss(prediction, label) # find out how well/wrong we were
        loss.backward()                     # backpropagate the loss
        self.optimizer.step()               # update the weights
        return (loss.item())

BATCH_SIZE = 32
training_data_loader = DataLoader(training_data, batch_size=BATCH_SIZE, shuffle=True)
testing_data_loader = DataLoader(testing_data, batch_size=BATCH_SIZE, shuffle=True)

# print(len(training_data))
# print(training_data[0][0].shape)
print(len(training_data_loader))
# print(len(training_data_loader.dataset))
# print(training_data_loader.dataset[0][0].shape)

pyTeen = PyTeen()
# training loop
# we want to call train repeatedly with the training data pairs (input, label)
EPOCH = 1
for i in range(EPOCH):
    k, total_loss = 0, 0
    for input, label in training_data_loader:
        # print(f'input: {input}\n')
        # print(f'label: {label}\n')
        total_loss += pyTeen.train(input, label)
        k += 1
    print(f'k is: {k}\n')
    print(f'total_loss for EPOCH {i} is: {total_loss}\n')
    # print(f'total_loss for EPOCH {i} is: {total_loss/len(training_data_loader)}\n')


