print("Welcome to the Competition!!")

play_game = input("Do you wish to play the game? ")

if play_game.lower() != "yes":
    quit()

print("Great!! Let's roll in :)")
score = 0

answer = input("What is the full form of MCU? ")

if answer.lower() == "micro controller unit":
    print('Correct answer!!!')
    score += 1
else:
    print('Incorrect answer!')

answer = input("What is the full form of MPU? ")

if answer.lower() == "micro processor unit":
    print('Correct answer!!!')
    score += 1
else:
    print('Incorrect answer!')

answer = input("What is the full form of FET? ")

if answer.lower() == "Field Effect Transistor":
    print('Correct answer!!!')
    score += 1
else:
    print('Incorrect answer!')

answer = input("What is the full form of LoRa? ")

if answer.lower() == "Long Range":
    print('Correct answer!!!')
    score += 1
else:
    print('Incorrect answer!')

answer = input("What is the full form of MOSFET? ")

if answer.lower() == "metal oxide semiconductor field effect transistor":
    print('Correct answer!!!')
    score += 1
else:
    print('Incorrect answer!')

if score >= 4:
    print("Very Good and your score is" + str(score))
else:
    print("Get Better")