import os
pwd = os.getcwd()
print('pwd is: ', pwd, '\n');
pwd = pwd + '/NSCCAI/codes/cars.csv'

# open the cars.csv file
file = open(pwd, 'r');
print(file.read(),'\n');
file_read_binary = open(pwd, 'rb');
print(file_read_binary.read());
# for line in file:
#     print(line);
# file.close();