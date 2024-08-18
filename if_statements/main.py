age = int(input("Enter your age to continue: "))
print(f"The age you had entered is {age}")
if age >= 100:
    print("Too old for the eligibility")
elif age >= 18:
    print("You are eligible to continue")
    name = input("Enter your name: ")
    if name == "":
        print("Enter a valid name for sake")
    else:
        print(f"The name you had entered is {name}")
        response = input("Would you like to have some food ? (Y/N): ")
        if response == "Y":
            print("What would you like to prefer?")
        else:
            print("Ok, Cool")
    online = True
    if online:
        print("You better hurry")
    else:
        print("You have enough time.")
elif age <= 0:
    print("Enter a valid age to continue")
else:
    print("You must be having minimum age of 18 to continue")
