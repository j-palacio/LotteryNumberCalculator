# Initialize list of numbers.
numbers = []

# Assign random numbers to list.
import random

for i in range(7):
    numbers.append(random.randint(0, 9))

# Display numbers in a single line.
for number in numbers:
# Separate current number from next number.
    print(number, end=' ')
print()
