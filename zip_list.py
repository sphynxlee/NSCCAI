names = ['bob', 'joe', 'susan', 'margaret']
age = [20, 30, 40, 50]

zip_result = zip(names, age)
print(type(zip_result))

# [('bob', 20), ('joe', 30), ('susan', 40), ('margaret', 50)]
print(f'listed zip_result: {list(zip_result)}')

list_result = list(zip_result)
print(f'list_result: {list_result}')


# (('bob', 20), ('joe', 30), ('susan', 40), ('margaret', 50))
tuple_result = tuple(zip_result)
print(f'tuple_result: {tuple(zip_result)}')


map_obj = map(list, list_result)
print(map_obj)

tuple_to_list = list(map_obj)


x = 'Elon'
y = 'twitter'
x,y = y,x
print(f'x is now {x} and y is now {y}')

pi = 3.141592653589793
print(f'pi is {pi:.2f}')

############################### dictionary
ml_dictionary = {
    "Supervised Learning": "A type of machine learning where the model learns from labeled data.",
    "Unsupervised Learning": "A type of machine learning where the model learns from unlabeled data.",
    "Feature Extraction": "The process of selecting relevant features from raw data for use in machine learning.",
    "Gradient Descent": "An optimization algorithm used to minimize the loss function during model training."
}
# Read
print(ml_dictionary["Supervised Learning"])
term = "Supervised Learning"
description = ml_dictionary.get(term, "Term not found")
print(f"{term}: {description}")
