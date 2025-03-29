class Car:
    """
    A class to represent a car.

    Attributes:
        make (str): The brand of the car (e.g., Toyota, Ford).
        model (str): The model of the car (e.g., Camry, Mustang).
        year (int): The manufacturing year of the car.
        color (str): The color of the car.
    """

    def __init__(self, make, model, year, color):
        """
        Initializes a Car object with the given attributes.

        Args:
            make (str): The car's brand.
            model (str): The car's model.
            year (int): The car's manufacturing year.
            color (str): The car's color.
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        """
        Simulates the car driving.
        """
        print(f'This {self.model} is driving.')

    def stop(self):
        """
        Simulates the car stopping.
        """
        print(f'This {self.model} has stopped.')

# Example usage:
my_car = Car("Toyota", "Camry", 2022, "Blue")
my_car.drive()  # Output: This Camry is driving.
my_car.stop()   # Output: This Camry has stopped.
