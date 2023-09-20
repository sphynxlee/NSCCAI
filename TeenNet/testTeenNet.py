import numpy as np
from .TeenNet import TeenNet

INPUT_NODES_NUM = 5
HIDDEN_NODES_NUM = 5
OUTPUT_NODES_NUM = 5

LEARNING_RATE = 0.03

tNet = TeenNet(INPUT_NODES_NUM, HIDDEN_NODES_NUM, OUTPUT_NODES_NUM, LEARNING_RATE, lambda x: np.maximum(0, x))
tNet.forward_pass([1,2,3,4,5])