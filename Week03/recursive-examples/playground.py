def f(a):
    print(a)

#  print(f(5))

# what is being printed out? 

# opt1: 5 
# opt2: None 
# opt3: Both opt1 and 2

def g(b):
    b = b+1 
    return b 

out = g(6)
# print(out) # 7
# print(g)
# print(g(9))

def sum_recursive(array):
    # BASE CASE
    if (len(array) == 1):
        return array[0]
    # RECURSIVE CASE
    return array[0] + sum_recursive(array[1:])

print(sum_recursive([4, 2, 1, 9, 10, 13]))










