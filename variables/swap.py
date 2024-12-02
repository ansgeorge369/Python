a = 5
b = 6

temp = a
a = b
b = temp

print(a, b)

#without temp

c =10
d = 8

c = c + d
d = c - d
c = c - d

print(c, d)

#anothe option is ^ c = c ^ d there will be no wastage of bits
# a, b = b, ias also possible