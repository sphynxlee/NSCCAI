# create a list of some interesting items
# for example: the car brands
cars_brand = ['Ford', 'Honda', 'Toyota', 'Mazda', 'Nissan']

# perform all CRUD operations on the cars_brand list
# add a new car brand
cars_brand.append('BMW')
print("add a new car brand: ", cars_brand)
# read a car brand
print("read a car brand 0: ", cars_brand[0])
# update a car brand
cars_brand[0] = 'Audi'
print("update a car brand 0: ", cars_brand)
# delete a car brand
del cars_brand[0]
print("delete a car brand 0: ", cars_brand)

# Extract all elements of the cars_brand list into a new list
cars_brand = ['Ford', 'Honda', 'Toyota', 'Mazda', 'Nissan']
print("reset cars_brand list: ", cars_brand)
cars_brand_new = []
for car_brand in cars_brand:
    cars_brand_new.append(car_brand)
print("extract all elements of the cars_brand list into a new list: ", cars_brand_new)

# function to reverse the list
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def reverse_list(list):
    reverse_list = []
    pointer = len(list) - 1
    while pointer >= 0:
        reverse_list.append(list[pointer])
        pointer -= 1
    return reverse_list
print("reverse the list: ", reverse_list(cars_brand))

# replace_in_list function
def replace_in_list(list, old, new):
    for i in range(len(list)):
        if list[i] == old:
            list[i] = new
    return list
print("replace old: Ford to new: Audi: ", replace_in_list(cars_brand, 'Ford', 'Audi'))
