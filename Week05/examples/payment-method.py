from collections.abc import Iterator

class DDWListIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # returns itself

    # abstract method of Iterator, implementation is enforced
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val


it = DDWListIterator([1, 2, 3])

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

for x in it: # we can also loop through the elements
    print(x)


    





