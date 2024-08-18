# while loop program

name = input("Enter the username: ")

while name == "":
    print("Enter a valid username")
    name = input("Enter the username: ")

print(f"The username you had entered is {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Enter a valid age to continue")
    age = int(input("Enter your age: "))

print(f"You had entered the age as {age}")

food = input("Which food do you prefer? OR press E to exit: ")

while not food == "E":
    print(f"You had preferred {food} as your first choice")
    food = input("Enter another food you wish to have: OR press E to exit: ")

print("Thankyou! See you soon!")