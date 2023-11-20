words = ['I', 'like', 'apples', 'He', 'likes', 'python', 'She', 'is', 'learning', 'NLP']

unique_words = set(words)
# print(unique_words)

word2int = dict(enumerate(unique_words))
# print(word2int.values())
# print(word2int.keys())
print(f'word2int is {word2int}')

int2word = dict(zip(word2int.values(), word2int.keys()))
print(f'int2word is {int2word}')

# number change to vector

import numpy as np

def one_hot_encoder(word, word2int):
    # word_vec = [0] * len(word2int)
    word_vec = np.zeros(len(word2int))
    word_index = word2int[word]
    word_vec[word_index] = 1
    return word_vec
