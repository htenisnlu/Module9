# Hikmet Tenis
# 08/31/2024
# Problem 4: Create a while loop that appends numbers divisible by 10 from 0 to 50 to a list.

tens = []
counter = 0

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(f"List of numbers divisible by 10: {tens}")
