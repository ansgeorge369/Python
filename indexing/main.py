# indexing - accessing elements of a sequence using []
#                [start : end : step]

aadhar_no = "1234-5678-9012-3456"
last_digits = aadhar_no[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
aadhar_no = aadhar_no[::-1]  # reverse string no
print(aadhar_no)