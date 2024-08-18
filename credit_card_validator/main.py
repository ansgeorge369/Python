# credit card validator program
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd position from right to left
# 3. Double every second digit from right to left
#              (If result is a two-digit number,
#                   add the numbers together to get a single digit number)
# 4. Sum the totals of steps 2 & 3.
# 5. If the sum is divisible by 10 then the credit card is valid.

sum_odd_digits = 0
sum_even_digits = 0
total = 0

card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

for i in card_number[::2]:
    sum_odd_digits += int(i)
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x

total = sum_even_digits + sum_odd_digits

if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
