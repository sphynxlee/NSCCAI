# Given a list of words, write a function that prints the one-hot encoding map
# and then generates and returns a one-hot encoded vector for the list.

import numpy as np

words = ['I', 'like', 'apples', 'He', 'likes', 'python', 'She', 'is', 'learning', 'NLP']
def one_hot_encode(words):
    # create a set of unique words
    unique_words = set(words)
    # create a dictionary of unique words
    word2int = dict(enumerate(unique_words))
    # create a dictionary of unique words
    int2word = dict(zip(word2int.values(), word2int.keys()))
    # create a one-hot encoded vector
    one_hot_vector = np.zeros(len(unique_words))
    # create a list of one-hot encoded vectors
    one_hot_vectors = []
    # loop through words
    for word in words:
        # reset one-hot encoded vector
        one_hot_vector = np.zeros(len(unique_words))
        # get index of word
        index = int2word[word]
        # set index to 1
        one_hot_vector[index] = 1
        # append one-hot encoded vector to list
        one_hot_vectors.append(one_hot_vector)
    # return list of one-hot encoded vectors
    return one_hot_vectors

print(one_hot_encode(words))