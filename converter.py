def length_converter():
    print("\nLength Conversion:")
    print("1. Meters to Feet")
    print("2. Kilometers to Miles")
    choice = input("Choose an option: ")

    if choice == '1':
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters = {feet:.2f} feet")
    elif choice == '2':
        km = float(input("Enter length in kilometers: "))
        miles = km * 0.621371
        print(f"{km} km = {miles:.2f} miles")


def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Grams to Ounces")
    choice = input("Choose an option: ")

    if choice == '1':
        kg = float(input("Enter weight in kg: "))
        pounds = kg * 2.20462
        print(f"{kg} kg = {pounds:.2f} pounds")
    elif choice == '2':
        grams = float(input("Enter weight in grams: "))
        ounces = grams * 0.035274
        print(f"{grams} g = {ounces:.2f} ounces")


def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    choice = input("Choose an option: ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print(f"{c}°C = {k:.2f}K")


def main():
    while True:
        print("\nUnit Converter Menu")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        option = input("Select a conversion category (1-4): ")

        if option == '1':
            length_converter()
        elif option == '2':
            weight_converter()
        elif option == '3':
            temperature_converter()
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
