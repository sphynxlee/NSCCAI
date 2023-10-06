import os
pwd = os.getcwd()
pwd = pwd + '/NSCCAI/codes/two_name_pairing/namesList.txt'
print(pwd)

file = open(pwd, 'r')
namesList = file.read().split('\n')
# print(f'length of namesList: {len(namesList)}')

isEven = True
if len(namesList) % 2 == 0:
    # print("The number of students is even.")
    isEven = True
else:
    print("The number of students is odd.")
    last_count = int(len(namesList) / 2)
    # print(f'The last count {last_count}')
    isEven = False

count = 0
for i in range(0, len(namesList)-1, 2):
    count += 1
    # print(count)
    if isEven:
        print(namesList[i], namesList[i+1])
    else:
        if count == last_count:
            print(namesList[i], namesList[i+1], namesList[i+2])
        else:
            print(namesList[i], namesList[i+1])



