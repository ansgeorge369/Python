name = input("What is your name? : ")
age = int(input("How old are you? : "))   # age in int
height = float(input("How tall are you? : "))  # height in float

print("Hello, " + name)
print("Confirming age as " + str(age))    # typecasting again back to string to print
print("Confirming age as " + str(height) + " cm tall")  # typecasting again back to float to print

ch = input('Enter a char : ')[0]
print(ch)  # only the first char will be taken into stack

result = eval(input("Enter the expression : "))
print(result)