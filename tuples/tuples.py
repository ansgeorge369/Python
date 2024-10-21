#tuple is immutable as compared to list
tup = (21, 31, 41)
print(tup)

print(tup[1])

test = (2, 5, 5, 3,1)
print(test.count(5))
print(test.index(5))

#set
set1 = {25, 65, 6, 32, 8, 76}
print(set1)   #there is no certain order to print

set2 = {22, 9, 64, 32, 5, 8, 9}
print(set2)  #if two same values are in set it will only be printed once. Indexing is also not supported. so value cannot be changed
set2.remove(9)
print(set2)
set2.clear()
print(set2)