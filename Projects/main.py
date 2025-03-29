# Banking Program

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    pass

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Welcome! You are entering Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter the operation you want to perform bw 1-4: ")

    if choice == '1':
        show_balance()

    elif choice == '2':
        deposit()

    elif choice == '3':
        withdraw()

    elif choice == '4':
        is_running = False

    else:
        print("Incorrect operation requested")

print("Thank you!! Have a nice Day!")