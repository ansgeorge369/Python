a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True (same reference)
print(a is c)   # False (different objects, same content)
