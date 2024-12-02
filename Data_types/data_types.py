# None
# Numeric - int, float, complex,bool
# Complex
# Bool
# Sequence - list, tuple, set, sting, range. No char str is used for char

num = 2.5
print(type(num))
num2 = 5
print(type(num2))
num3 = 6+5j
print(type(num3))

#type conversion
a = 5.2
b = int(a)
print(type(b))
k = float(b)
print(k)

k = 8
c = complex(k,b)
print(c)
print(b<k)

print(int(True))

lst = [32,25,65]
print(type(lst))

set1 = {6,8,9}
print(type(set1))

t = (9,8,7)
print(type(t))

str1 = "ans"
print(type(str1))

range(10)
print(range(10))
print(list(range(10)))

#print even only. list can take three parameters
print((list(range(0,20,2))))

#dictonary

z = {'ans':'iqo neo6', 'radhika': 'moto'}
print(z)
print(z.keys())
print(z.values())
print(z.get('radhika'))