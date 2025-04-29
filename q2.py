import math

#Write a function to add two numbers.
def add(a,b):
    return a+b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = add(a, b)
print("The total sum is: ", c)

#Write a function to find the factorial of a number.
def factorial(n):
    fact = 1
    while(n > 0):
        fact = fact * n
        n = n - 1
    return fact

d = int(input("Enter a number: "))
e = factorial(d)
print("Factorial of the given number is ", e)

#Reverse a string without using built-in functions.
def reverse_string(data):
    return data[::-1]

data = input("Enter a string: ")
reversed_data = reverse_string(data)
print("The reversed string is ", reversed_data)