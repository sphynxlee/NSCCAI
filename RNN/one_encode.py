import numpy as np

def one_hot_encoder(words):
    print(list(enumerate(words)))
    unique_words = list(set(words))
    encoding_map = {word: i for i, word in enumerate(unique_words)}

    # output encoding map
    for word, i in encoding_map.items():
        print(f'slot {i+1}: {word}')

    # one hot encoding
    one_hot_vectors = np.zeros((len(words), len(unique_words)), dtype=np.int32)
    for i, word in enumerate(words):
        one_hot_vectors[i, encoding_map[word]] = 1
    return one_hot_vectors

cars = ['BMW', 'Benz', 'Benz', 'Tesla', 'Toyota']
print(one_hot_encoder(cars))