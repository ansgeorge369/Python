# import math

# #Write a function to add two numbers.
def add(a,b):
    return a+b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = add(a, b)
print("The total sum is: ", c)

# #Write a function to find the factorial of a number.
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

#Count the number of vowels in a string
def vowels_string(data):
    counter = 0
    for i in data:
        if(i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'O' or i == 'U'):
            counter +=1
    return counter

check = input("Enter a string: ")
count = vowels_string(check)
print("The total number of vowels present in the string is ", count)

#Create a list of 5 numbers and find their sum.Find the largest number in a list.
my_list = [1, 2, 3, 4, 5]
res = sum(my_list)
print("Sum of the list is ",res)
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print("The largest number in the list is ", largest) 

#Create a dictionary with 3 key-value pairs and print all keys.Write a program to check if a key exists in a dictionary.
my_dict = {"brand" : "Ford",
           "model" : "Mustang",
           "year" : "1969"}
print("Keys in the dictonary is ", my_dict.keys())
key = 'year'
print(key in my_dict)

#Check if a string is a palindrome.
def is_palindrome(data):
    if data == data[::-1]:
        print("The given string is Palindrome")
    else:
        print("The given string is not palindrome")
        
data_to_check = input("Enter the string to check: ")
is_palindrome(data_to_check)

#Generate a multiplication table for a number (like 5 × 1 = 5, etc.).
def multiplication(num):
    end = 10
    for i in range(1, end + 1):
        result = num * i
        print(f"{num} x {i} = {result}")
        
mul = int(input("Enter a number to form multiplication table: "))
multiplication(mul)

#Write a program to find prime numbers between 1 and 100.
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

#Write a program to count how many times each character appears in a string.

def count_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

text = input("Enter a string: ")
result = count_characters(text)

print("Character counts:")
for char, count in result.items():
    print(f"'{char}': {count}")