unit = input("What is the unit of temperature being given as input Celsius or Fahrenheit C / F: ")
if unit not in ["F", "C"]:
    print("Invalid Unit for measurement")
elif unit in ["F", "C"]:
    value = float(input("Enter the value: "))
    if unit == "F":
        temp = round((value - 32) * 5/9, 2)
        print(f"Temperature in Celsius is {temp} °C")
    elif unit == "C":
        temp = round((9 * value) / 5 + 32, 2)
        print(f"Temperature in Fahrenheit is {temp} °F")  # Alt+0176 = °