

def make_class(*args):
    class MyClass:
        attr = []
        for i in args:
            attr.append(i)

        def __init__(self, *args):
            print(MyClass.attr)
            for i, value in enumerate(args):
                setattr(self, MyClass.attr[i], value)
    return MyClass


class Animal:
    def __init__(self, name, species, age, health, weight, color):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.weight = weight
        self.color = color


Animel = make_class("name", "species", "age", "health", "weight", "color")

dog1 = Animal("Bob", "Dog", 5, "good", "50lb", "brown")
dog2 = Animel("Bob", "Dog", 5, "good", "50lb", "brown")
print(dog1.name, dog2.name)
print(dog1.species, dog2.species)
print(dog1.age, dog2.age)
print(dog1.health, dog2.health)
print(dog1.weight, dog2.weight)
print(dog1.color, dog2.color)
print(dog2.__dict__)