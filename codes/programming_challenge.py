# Programming Chanllenge

# function called find_pairs(), which takes an integer array and a target number,
# Your job is to return a pair of indices. They are the indices of two numbers
# in the array that add up to the target number.

# You can assume that 1) there are only 2 numbers in the array that 'work'
# and you cannot use the same number twice.
def find_pairs(number_list, target):
    pairs = {}
    for i in range(len(number_list)):
        for j in range(i+1, len(number_list)):
            if (number_list[i] == target - number_list[j] and number_list[i] != number_list[j]) :
                pairs[i] = number_list[i]
                pairs[j] = number_list[j]
                return pairs

arr = [2,2,1,3,5]
res = find_pairs(arr, 4)
print(res)



