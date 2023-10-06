import sys

class Animal:
    def __init__(self: "Animal", name: str, color: str, noise: bool = False) -> None:
        self.name = name
        self.color = color
        self.noise = noise

    def make_noise(self: "Animal", noise: bool) -> None:
        print(f"{self.name} Animal is making noise")
        self.noise = noise

    # def __str__(self: "Animal") -> str:
    #     return f"{self.name} is {self.color} and makes noise: {self.noise}"

# subclass of Animal: mammal
class Mammal(Animal):
    def __init__(self: "Mammal", name: str, color: str, noise: bool = False) -> None:
        super().__init__(name, color, noise)
        self.name = name
        self.color = color
        self.noise = noise

    def make_noise(self: Animal, noise: bool) -> None:
        # super().make_noise(noise)
        print(f"{self.name} is a Mammal, did it cause any noise? {'Yes' if noise else 'No'}")



chicken = Animal("Chicken", "White")
print("chicken is: ", chicken)


dog = Mammal("Dog", "Brown")
dog.make_noise(True)
# to string
# print("dog is: ", dog)
