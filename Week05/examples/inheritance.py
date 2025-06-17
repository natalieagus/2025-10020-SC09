

class Animal:
    def speak(self):
        return "Some sound"

    def move(self): 
        return "Animal is moving"

class Dog(Animal):
    def speak(self): # type: ignore
        # print(super().speak())
        return "Bark"

class Puppy(Dog):
    # OVERRIDE
    def speak(self): # type: ignore
        # print(super().speak())
        return "Yip"
    # OVERRIDE
    def move(self): 
        print(super().move()) # this will call Dog move(), but since Dog does not have move(), it will find and call Animal move() 
        return "Puppy is moving"

p = Puppy()
print(p.speak())
print(p.move())





