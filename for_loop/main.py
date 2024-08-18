id_card = "0123-9874-5632-1023"
for i in reversed(id_card):
    print(i)

for i in range(0, 20):
    if i == 13:
        continue            # skips one part of iteration
    else:
        print(i)

for i in range(0, 20):
    if i == 13:
        break
    else:
        print(i)