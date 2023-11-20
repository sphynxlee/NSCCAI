import torch
from torch import nn, optim
import torch.nn.functional as F

class SequenceRNN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        # self.embedding = nn.Embedding(10000, 128)
        self.embedding = nn.Embedding(vocab_size, embedding_size)
        self.rnn = nn.LSTM(embedding_size, embedding_size, batch_first=True)
        self.ev2 = nn.Linear(embedding_size, vocab_size)