# 1221
# 12321
# abba
# abcba

def isPalindrome(test_str) -> bool:
    test_str = str(test_str)

    if len(test_str) <= 1:
        return True
    else:
        if test_str[0] == test_str[-1]:
            return isPalindrome(test_str[1:-1])
        else:
            return False

# print(isPalindrome('abba'))
# print(isPalindrome(1234321))
test_str = input('Please input a string which used to test palindrome: ')
res = isPalindrome(test_str)
print(f'{test_str} is palindrome: {res}')