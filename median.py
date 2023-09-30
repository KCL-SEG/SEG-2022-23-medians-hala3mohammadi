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
print(numbers)

numbers.sort()     
length = len(numbers)
median=0.0

if length%2!=0:
    median = numbers[length//2]
else:
    median = (numbers[length//2] + numbers[(length//2)-1]) / 2

print(f"The median is {median}")
