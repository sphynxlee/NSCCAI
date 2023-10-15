def decimal_to_binary (number, remain_list = []):
    number = int(number)

    left = int(number / 2)
    remain = number % 2

    remain_list.append(remain)

    if left > 0:
        return decimal_to_binary(left, remain_list)
    else:
        remain_list.reverse()
        return remain_list

print(decimal_to_binary(52))
