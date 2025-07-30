import numpy

p = numpy.ones((5,1))
new_p = numpy.where(p >= 0.5, 0, 1)
print("new_p", new_p)

print(p)