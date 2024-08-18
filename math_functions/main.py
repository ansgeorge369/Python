import math

# Total = 10
# Total = Total+10
# Total += 10
# Total = Total-10
# Total -= 10
# Total = Total*5
# Total *= 5
# Total = Total/2
# Total /= 2
# remainder = Total % 3
# print(remainder)

# x = 3.1421
# y = -5
# z = 32
# result = round(x)
# absolute_value = abs(y)
# power = pow(5, 3)
# max_value = max(x, y, z)
# min_value = min(x, y, z)
# sroot = math.sqrt(a)
# print(result)
# print(absolute_value)
# print(power)
# print(max_value)
# print(min_value)
# print(math.pi)
# print(math.e)
# print(sroot)

r = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * r
print(f"The circumference of the circle is {round(circumference, 3)}")

# Area of a circle

ra = float(input("Enter the radius of the circle: "))
area = math.pi * pow(ra, 2)
print(f"The area of the circle is {round(area,3)} cm^2")

# Hypotenuse of a Right Triangle

a = float(input("Enter the value of side A: "))
b = float(input("Enter the value of side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The Hypotenuse of the triangle is {round(c, 2)} cm")