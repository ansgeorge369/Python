# name = input("Enter your name: ")
# result = len(name)
# result1 = name.find("e")
# result2 = name.rfind("e")
# name = name.upper()
# name2 = name.lower()

# print(result)
# print(result1)
# print(result2)
# print(name)
# print(name2)
# print(help(str))


# valid username
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("The username can contain only 12 characters")
elif not username.find(" ") == -1:
    print("Username cannot contain spaces in between!")
elif not username.isalpha():
    print("Username cannot contain numeric values")
else:
    print(f"Welcome {username} to the community")