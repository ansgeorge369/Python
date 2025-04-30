def is_palindrome(data):
    return data == data[::-1]


data = input("Enter a data to check palindrome or not: ")

if is_palindrome(data):
    print("It is a palindrome")
else:
    print("It is not a palindrome")