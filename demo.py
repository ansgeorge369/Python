# ----------------------------------------------
# Python Program to Demonstrate:
# - Variable declaration
# - Primitive & non-primitive data types
# - Input/output operations
# - Operators (arithmetic, logical, comparison)
# - Comments and indentation
# ----------------------------------------------

# 🔸 Output operation using print()
print("Welcome to Python Basics Demonstration!\n")

# 🔹 Variable declaration with primitive data types
name = input("Enter your name: ")             # String (str)
age = int(input("Enter your age: "))          # Integer (int)
height = float(input("Enter your height: "))  # Float (float)
is_student = True                             # Boolean (bool)

# 🔸 Displaying variable types (output and type checking)
print(f"\nHello {name}, here are your details:")
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Student:", is_student, "| Type:", type(is_student))

# 🔹 Arithmetic operations
year_of_birth = 2025 - age                     # Using subtraction operator
bmi = height / (1.75 ** 2)                     # Division and exponentiation
print(f"Estimated Year of Birth: {year_of_birth}")
print(f"Estimated BMI (with dummy height 1.75m): {round(bmi, 2)}")

# 🔹 Comparison and logical operators
is_adult = age >= 18                           # Comparison operator
eligible = is_adult and is_student             # Logical AND operator
print(f"Are you an adult student? {eligible}")

# 🔹 Assignment operators
score = 10
score += 5                                     # Equivalent to score = score + 5
print("Score after bonus points:", score)

# 🔹 Using non-primitive data structures

# List: ordered and mutable
subjects = ["Math", "Science", "Python"]
subjects.append("AI")                          # Adding new subject
print("\nSubjects List:", subjects)

# Tuple: ordered and immutable
coordinates = (10.5, 20.5)
print("Coordinates (Tuple):", coordinates)

# Set: unordered and unique
skills = {"Python", "ML", "Python"}            # Duplicate "Python" will be removed
print("Unique Skills (Set):", skills)

# Dictionary: key-value pairs
student_info = {
    "Name": name,
    "Age": age,
    "Is_Student": is_student,
    "Subjects": subjects
}
print("Student Info (Dictionary):", student_info)

# 🔹 Type conversion example
age_str = str(age)                             # Convert int to string
print("Age as string:", age_str, "| Type:", type(age_str))

# 🔹 NoneType
undefined_value = None
print("Undefined variable (NoneType):", undefined_value, "| Type:", type(undefined_value))

# ✅ End of program
print("\nThank you for using the demo program!")
