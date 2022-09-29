"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
i = (len(numbers) - 1) // 2
print(numbers[i] if len(numbers) % 2 == 0 else (numbers[i] + numbers[i+1])/2)