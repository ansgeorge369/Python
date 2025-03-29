"""
This script demonstrates the use of the Car class by creating multiple car objects 
and displaying their details. Each car object represents a different car brand, model, 
year, and color. The script then calls the `drive` and `stop` methods to simulate 
driving behavior.

Use Cases:
- Creating and managing multiple car objects.
- Simulating car actions such as driving and stopping.
- Demonstrating object-oriented programming (OOP) concepts like classes and objects.
"""

# Importing the Car class from another file (car.py)
from car import Car  

# Creating three Car objects with different attributes
car1 = Car("BMW", "X5", 2018, 'Red')        # BMW X5, manufactured in 2018, Red color
car2 = Car("Audi", "A4", 2019, 'Black')      # Audi A4, manufactured in 2019, Black color
car3 = Car("Mercedes", "S500", 2017, 'White') # Mercedes S500, manufactured in 2017, White color

# Iterating through all car objects and displaying their details
for car in [car1, car2, car3]:
    print("---------------")  # Separator for readability
    
    # Printing car attributes
    print(f"Make: {car.make}")   # Displaying the car's brand (e.g., BMW, Audi)
    print(f"Model: {car.model}") # Displaying the car's model (e.g., X5, A4)
    print(f"Year: {car.year}")   # Displaying the manufacturing year
    print(f"Color: {car.color}") # Displaying the car's color
    
    # Simulating car actions
    car.drive()  # Calling the drive method
    car.stop()   # Calling the stop method
