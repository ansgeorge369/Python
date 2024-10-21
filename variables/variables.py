a = 5
print(a)

name = 'youtube'
print((name + ' rocks'))

print(name[0])
print(name[-1])
print(name[0:2])
print(name[1:4])
print(name[1:])
print(name[:4])

# strings in python is immutable ie once the values are assigned name[0] = u cannot be done

print('my ' + name[3:])
myname = 'Ans'
print(len(myname))

num = 5
print(id(name))    #get address of name
print(id(num))

b = a
print(id(a))
print(id(b))   #if different variables have same data the address will be same. so more memory efficient
print(id(5))   #only if data changes the address will be changed

a =9
print(id(a))

#there no concept of constant in python instead we can show the intension by writing capitals eg: PI = 3.14

PI = 3.14
print(type(PI))
print(type(a))