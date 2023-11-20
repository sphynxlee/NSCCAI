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
