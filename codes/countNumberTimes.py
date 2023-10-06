# find the most appeared number in a list, return the number and the times it appeared

def count_number_times(lists):
    for i in range(0, len(lists) - 1):
        count = 0
        print(f'list is: {lists}')
        j = i + 1
        for j in range(i+1, len(lists) - 1):
            # print(f'list j is: {lists[j]}')
            if lists[i] == lists[j]:
                print(f'j is: {j}')
                count += 1
                print(lists[i], count)
                #  delete current list[j] element
                lists.pop(j)

    # print(lists)

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]
count_number_times(lists)