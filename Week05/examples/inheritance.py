

class Animal:
    def speak(self):
        return "Some sound"

    def move(self, inp): 
        return "Animal is moving"

class Dog(Animal):
    def speak(self): # type: ignore
        # print(super().speak())
        return "Bark"

class Puppy(Dog):
    def __init__(self):
        self.attribute = "something"
    # OVERRIDE
    def speak(self): # type: ignore
        # print(super().speak())
        return "Yip"
    # OVERRIDE
    def move(self): 
        return "Puppy is moving"

    @property 
    def some_prop(self):
        return 5

p = Puppy()
# print(p.speak())
print(isinstance(Dog, Animal))
# print(p.move())
# print(Puppy.some_prop.fget.__name__)
# print(Puppy.attribute.fget.__name__)




