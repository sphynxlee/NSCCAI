# No.1
def sentences_alignment (sentence_lists):
    len_lists = []

    for i in range(len(sentence_lists)):
        len_lists.append(len(sentence_lists[i]))

    max_len = max(len_lists)

    for i in range(len(sentence_lists)):
        if len_lists[i] < max_len:
            for j in range(max_len - len_lists[i]):
                sentence_lists[i] += ' '

    return sentence_lists

sentence_lists = [
    'I like apples',
    'He likes python',
    'She is learning NLP'
]
print(sentences_alignment(sentence_lists))

# No.2
sentence_lists = [
    'i like apples',
    'He likes python',
    'She is learning NLP'
]

def unique_words (sentence_lists):
    result_sentences = []
    for i in range(len(sentence_lists)):
        result_sentences.append(set(sentence_lists[i]))

    return result_sentences

print(unique_words(sentence_lists))

# No.3
def get_unique_chrs(sentences):
    chrs = set(''.join(sentences))
    return (sorted(chrs))

sentences = ['I like apples', 'He likes python', 'She is learning NLP']
print(get_unique_chrs(sentences))

# No.4
letters = [' ', 'H', 'I', 'L', 'N', 'P', 'S', 'a', 'e', 'g', 'h', 'i', 'k', 'l', 'n', 'o', 'p', 'r', 's', 't', 'y']

def get_int_map(vocab):
    int2chr = dict(enumerate(vocab))
    return (int2chr)
print(get_int_map(letters))

letters = [' ', 'H', 'I', 'L', 'N', 'P', 'S', 'a', 'e', 'g', 'h', 'i', 'k', 'l', 'n', 'o', 'p', 'r', 's', 't', 'y']
def sorted_letters(letters):
    result = {}
    for i in range(len(letters)):
        result[i] = letters[i]
    return result
print(sorted_letters(letters))

# No.5
obj = {0: ' ', 1: 'H', 2: 'I', 3: 'L', 4: 'N', 5: 'P', 6: 'S', 7: 'a', 8: 'e', 9: 'g', 10: 'h', 11: 'i', 12: 'k', 13: 'l', 14: 'n', 15: 'o', 16: 'p', 17: 'r', 18: 's', 19: 't', 20: 'y'}
def reverse_key_value (obj):
    result = {}
    for key, value in obj.items():
        result[value] = key
    return result
print(reverse_key_value(obj))
