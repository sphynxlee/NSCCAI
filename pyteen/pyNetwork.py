import torch
from torch import nn, optim

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

    def predict(self, input):
        with torch.no_grad():
            pred = self.forward(input)
            return (torch.argmax(pred, axis=-1))

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
