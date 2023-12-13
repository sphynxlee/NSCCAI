# pascal's triangle
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1


def pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        # add n spaces to the left of the first row
        first_row = [1]
        print(first_row)
        return [first_row]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i]+last_row[i+1])
        new_row += [1]
        print(new_row)

        result.append(new_row)
    return result

print(pascal_triangle(5))