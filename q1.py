#Write a program to print "Hello, World!"
print("Hello World!")

#Take the user's name as input and greet them.
name = input("Please Enter your name: ")
print("Hello ", name)

#Create two variables a and b and swap their values.
a = 5
b = 6
print("values before swap: ", a,b)
temp = a
a = b
b = temp
print("Values after swap: ", a, b)

#Find the data type of a user-inputted value.
value = input("Enter a data: ")
print("Type of value given is ", type(value))

#Write a program to check if a number is positive, negative, or zero.
number_to_check = int(input("Enter an number: "))
if number_to_check > 0:
    print("The number is a positive number..")
elif(number_to_check == 0):
    print("The given number is zero")
else:
    print("The number is a negative number..")
    
#Check whether a number is even or odd.
n = int(input("Enter a number: "))
if(n%2 == 0):
    print("The number is even..")
else:
    print("The number is an odd number..")
    
#Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Print even numbers between 1 and 20 using a while loop.
j = 1
while j <=20:
    if(j % 2 == 0):
        print(j)
    j += 1