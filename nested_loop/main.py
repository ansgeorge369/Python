for i in range(3):
    for j in range(1, 10):
        print(j, end=" ")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol needed: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()