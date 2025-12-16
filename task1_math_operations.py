# Task 1: Basic Mathematical Operations

# Taking two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division = "Error! Cannot divide by zero."

# Displaying results
print("\n----- Results -----")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
