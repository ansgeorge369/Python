#  A = P(1+(r/n))t
#  A = Total repayable amount
#  P = Principal amount that is taken
#  r = interest rate
#  t = Total tenure

principle = 0
interest_rate = 0
tenure = 0

while principle <= 0:
    principle = float(input("Enter the amount: "))
    if principle <= 0:
        print(f"The principle amount cannot be less than or equal to 0.")

print(f"The principle amount you had entered is {principle}")

while interest_rate <= 0:
    interest_rate = float(input("Enter the interest rate that you are planning to take the principle: "))
    if interest_rate <= 0:
        print(f"The interest rate cannot be less than or equal to 0.")

print(f"The interest rate you had entered is {interest_rate}")

while tenure <= 0:
    tenure = int(input("Enter the tenure in years: "))
    if tenure <= 0:
        print(f"The tenure cannot be less than 0.")

print(f"The tenure for the repayment you had entered is {tenure}")

total = principle * pow((1 + interest_rate/100), tenure)
print(f"The total amount for principle {principle} for the time of {tenure} is $ {total : .2f}")