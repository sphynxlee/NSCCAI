
def decimal_to_binary (number, remain_list = []):
    number = int(number)

    left = int(number / 2)
    remain = number % 2

    remain_list.append(remain)

    while left > 0:
        decimal_to_binary(left, remain_list)
        return remain_list.reverse()

print(decimal_to_binary(52))