import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__() # super() 函数是用于调用父类(超类)的一个方法。
        # 1 input image channel, 6 output channels, 5x5 square convolution
        # kernel
        # 卷积层1
        self.conv1 = nn.Conv2d(1, 6, 5) # 1个输入通道，6个输出通道，5x5的卷积核
        # 卷积层2
        self.conv2 = nn.Conv2d(6, 16, 5) # 6个输入通道，16个输出通道，5x5的卷积核
        # 全连接层1
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120) # 16*5*5个输入，120个输出, 5*5是卷积后的图像大小, 5*5 from image dimension
        # 全连接层2
        self.fc2 = nn.Linear(120, 84)
        # 全连接层3
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window, 2x2的最大池化
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2)) # 卷积->激活->池化
        # If the size is a square you can only specify a single number
        # 如果是正方形，可以只指定一个数字
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        # view()函数作用是将一个多行的Tensor,拼接成一行
        x = x.view(-1, self.num_flat_features(x))
        # 全连接层1->激活
        x = F.relu(self.fc1(x))
        # 全连接层2->激活
        x = F.relu(self.fc2(x))
        # 全连接层3
        x = self.fc3(x)
        return x

    # 计算输入的特征数
    # calculate the number of features in a tensor
    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension, 除了批量维度的其他维度
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

net = Net()
print(net)