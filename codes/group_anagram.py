# input_words = ["listen", "silent", "enlist", "hello", "world", "wordl"]
# output = [["listen", "silent", "enlist"], ["hello"], ["world", "wordl"]]

def group_anagrams(arr):
    result_arr = []
    for i in range(len(arr)):
        current_element = arr[i]
        group_arr = []
        group_arr.append(current_element)
        arr = arr[1:]

        for j in range(len(arr)):
            if ''.join(sorted(current_element)) == ''.join(sorted(arr[j])):
                group_arr.append(arr[j])
                arr.pop(i)
        result_arr.append(group_arr)
    return result_arr


input_words = ["listen", "silent", "enlist", "hello", "world", "wordl"]
print(group_anagrams(input_words))

