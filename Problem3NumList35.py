# Hikmet Tenis
# 08/31/2024
# Problem 3: Using a while loop, ask the user to enter a number until the sum of the list is greater than 100.

numbers = []
total = 0

while total <= 100:
    number = int(input("Enter a number: "))
    numbers.append(number)
    total += number

print(f"Final list of numbers: {numbers}")
print(f"Sum of the numbers: {total}")
