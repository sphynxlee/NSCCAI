def decimal_to_binary (number, remain_list = []):
    number = int(number)

    left = int(number / 2)
    remain = number % 2

    remain_list.append(remain)

    if left > 0:
        return decimal_to_binary(left, remain_list)
    else:
        remain_list.reverse()
        binary_number = ''.join([str(x) for x in remain_list])
        return binary_number

print(decimal_to_binary(52))
