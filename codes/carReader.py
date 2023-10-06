import os
pwd = os.getcwd()
print('pwd is: ', pwd);
pwd = pwd + '/NSCCAI/codes/cars.csv'

# open the cars.csv file
file = open(pwd, 'r');
print(file.read());
# for line in file:
#     print(line);
# file.close();