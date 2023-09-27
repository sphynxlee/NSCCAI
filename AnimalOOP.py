import sys
from typing import Any


class Animal:
    def __init__(self: "Animal", name: str, color: str, noise: bool = False) -> None:
        self.name = name
        self.color = color
        self.noise = noise

    def make_noise(self: "Animal", noise: bool) -> None:
        self.noise = noise

    def __str__(self: "Animal") -> str:
        return f"{self.name} is {self.color} and makes noise: {self.noise}"

    def __add__(self: "Animal", other: "Animal") -> "Animal":
        # print(f"{self}")
        # print(f"{other}")
        return Animal("Monster", "Green", True)

    def __sub__(self: "Animal", other: "Animal") -> "Animal":
        # print(f"{self}")
        # print(f"{other}")
        return Animal("Monster", "Green", False)

    def __eq__(self: "Animal", other) -> bool:
        return self.name == other.name and self.color == other.color and self.noise == other.noise

    # size of Animal instance
    def __sizeof__(self: "Animal") -> int:
        return sys.getsizeof(self.name) + sys.getsizeof(self.color) + sys.getsizeof(self.noise)



dog = Animal("Dog", "Brown")
dog.make_noise(True)
# to string
print("dog is: ", dog)

cat = Animal("Cat", "White")
cat.make_noise(True)
# to string
print("cat is: ", cat)

# add two animals together
monster = dog + cat
print("Add, monster is: ", monster)

# subtract two animals
monster = dog - cat
print("Subtract, monster is: ", monster)

# compare two animals
result = dog == cat
print("Compare result is: ", result)

# print the size of an animal
print("size of dog is: ", sys.getsizeof(dog))