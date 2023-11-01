# write a function to find the contiguous sub array with the largest sum
# Kadane’s Algorithm
arr = [1, 6, -3, 22, -7, 4, 5, 99]

def max_subarray(arr):
    pass
    # max_sum = 0
    max_sum = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_sum = sum(arr[i:j+1])
            if sub_sum > max_sum:
                max_sum = sub_sum
    return max_sum

print(max_subarray(arr))