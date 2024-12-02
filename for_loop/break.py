#break

# available = 5
# x = int(input("How many candy's do you want? "))
#
# i = 1
# while i <= x:
#     if i > available:
#         print("Out of stock!!")
#         break
#     print("Candy")
#     i = i + 1
#
# print("Bye")


#continue
# for i in range(1, 101):
#
#     if i % 3 ==0 or i % 5 ==0:
#         continue
#     print(i)
#
# print("Bye")

#pass. Print only even
# for i in range (1, 101):
#     if i % 2 != 0:
#         pass
#     else:
#         print(i)

# continue skip the iteration
# for i in range(5):
#     if i == 3:
#         continue
#     print("Hello", i)

#break breaks the loop when condition is met, entire loop skips
# for i in range(5):
#     if i == 3:
#         break
#     print("Hello", i)

#pass - To keep a function empty after declaration
for i in range(5):
    if i == 3:
        continue
    print("Hello", i)

def func():
    pass