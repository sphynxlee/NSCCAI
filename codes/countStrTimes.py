def count_string_times(lists, str):
    count = 0
    for i in lists:
        if i == str:
            count += 1
    return count

lists = ['tom', 'jerry', 'tom', 'mike', 'jerry', 'tom']
print(count_string_times(lists, 'tom'))
