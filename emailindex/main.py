email = input("Please enter your email: ")

index = email.index("@")
user_name = email[:index]
domain_name = email[index + 1:]
print(f"Your username is {user_name} and domain name is {domain_name}")