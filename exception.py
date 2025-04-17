# Program demonstrating various exception types
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print("Result:", result)
    finally:
        print("End of division attempt.")
divide(10, 0)
# Raising and catching a custom exception
class UnderAgeError(Exception):
    pass

def validate_voter(age):
    if age < 18:
        raise UnderAgeError("You must be at least 18 to vote.")
    return "Eligible to vote"
try:
    print(validate_voter(16))
except UnderAgeError as e:
    print("Custom Exception:", e)
