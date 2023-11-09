import torch
from torch import nn,optim


class PyTeen(nn.Module):
  def __init__(self):
    super().__init__()
    self.layers = nn.Sequential(
      nn.Conv2d(1,6,5,padding=2),
      nn.ReLU(),
      nn.MaxPool2d(2,stride=2),

      nn.Conv2d(6,16,5,padding=0),
      nn.ReLU(),
      nn.MaxPool2d(2,stride=2),

      nn.Flatten(),
      nn.Linear(400,120),
      nn.Linear(120,84),
      nn.Linear(84,10)
    )
    self.loss = nn.CrossEntropyLoss()
    self.optimizer = optim.Adam(self.parameters())
   #self.to(torch.device(DEVICE)) #gpu

  def forward(self,input):
    return(self.layers(input))

  def predict(self,input):
    with torch.no_grad():
      pred = self.forward(input)
      return(torch.argmax(pred,axis=-1))  # type: ignore

  def train(self,input,label):
    self.optimizer.zero_grad()
    pred = self.forward(input)
    loss = self.loss(pred,label)
    loss.backward()
    self.optimizer.step()
    return(loss)