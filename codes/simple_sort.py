# for i = 1 to n do
#     for j = 1 to n do
#         if a[i] < a[j] then
#             swap a[i] and a[j]

# number_list = ['55', '89', '23', '13', '34', '45', '56', '17', '8', '29']
number_list = [55, 89, 23, 13, 34, 45, 56, 17, 8, 29]

for i in range(len(number_list)):
    for j in range(len(number_list)):
        if number_list[i] < number_list[j]:
            temp = number_list[i]
            number_list[i] = number_list[j]
            number_list[j] = temp
print(number_list)