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
n = len(numbers)
m = n // 2

if n % 2 == 1:
    print(numbers[m])
else:
    print((numbers[m] + numbers[m-1]) / 2)
