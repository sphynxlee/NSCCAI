A = [['a','b','c'],
    ['d','e','f'],
    ['g','h','i']]

At = [[row[i] for row in A] for i in range(len(A))]
print(At)

