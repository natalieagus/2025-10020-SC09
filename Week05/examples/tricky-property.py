class Example:
    def __init__(self):
        self._value = 1

    @property
    def value(self):
        print("getter")
        return self._value

    @value.setter
    def value(self, new):
        print("setter")
        self._value = new


e = Example()
e.value = 5            # (1)
print(e.value)         # (2)

Example.value = 42     # (3)   
print(e.value)         # (4)


