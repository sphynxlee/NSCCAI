# create a function that takes an array/list. It should then print out all __unique__ pairs of numbers in the list.
# [1,2,3,4,5,6,7]:
# [1,2], [1,3], [1,4], [1,5], [1,6], [1,7]
# [2,3], [2,4], [2,5], [2,6], [2,7]
# [3,4], [3,5], [3,6], [3,7]
# [4,5], [4,6], [4,7]
# [5,6], [5,7]
# [6,7]
# time complexity: O(n^2)
# space complexity: O(n^2)
def unique_pairs_in_list(list):
    result_arr = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] != list[j] and [list[i], list[j]] not in result_arr:
                result_arr.append([list[i], list[j]])
    return result_arr

res1 = unique_pairs_in_list([1,2,3,4,5,6,7])
# print(res1)

res2 = unique_pairs_in_list([1,2,3,4,5,5,6])
print(res2)

# Caesar Cipher/ROTn
# http://sticksandstones.kstrom.com/appen.html
def caesar_encrypt(str, n):
    is_upper = False
    if str.isupper():
        is_upper = True
        str = str.lower()
    result = ""
    if n > 26:
        n = n % 26

    for i in range(len(str)):
        if ord(str[i]) + n > 122:
            result = result + chr(ord(str[i]) + n - 26)
        elif str[i] != "":
            result = result + chr(ord(str[i]) + n)

    if is_upper:
        return result.upper()

    return result

res1 = caesar_encrypt("dean", 2)
print(res1)
res2 = caesar_encrypt("DEAZ", 2)
print(res2)

def caesar_decrypt(str, n):
    is_upper = False
    if str.isupper():
        is_upper = True
        str = str.lower()
    result = ""
    if n > 26:
        n = n % 26
    for i in range(len(str)):
        if ord(str[i]) - n < 97:
            result = result + chr(ord(str[i]) + 26 - n)
        elif str[i] != "":
            result = result + chr(ord(str[i]) - n)

    if is_upper:
        return result.upper()

    return result

res1 = caesar_decrypt("dean", 2)
print(res1)
res2 = caesar_decrypt("DEAZ", 2)
print(res2)