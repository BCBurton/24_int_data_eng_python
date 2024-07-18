# Python Refresher Script

# Variables and Data Types 
a = 100  # Integer
b = 32.14  # Float
c = "Hello, YOURNAME!"  # String
d = True  # Boolean

# Basic Operations in Python
sum = a + b  # Addition
difference = a - b  # Subtraction
product = a * b  # Multiplication
quotient = a / b  # Division
print(sum)
print(difference)

# Control Structures
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Loop
for i in range(5):
    print(i)

# Function Definition
def greet(name):
    return f"Hello, {name}!"

# Function Call
print(greet("Texas is the best state!"))

# Importing Modules
import math
print(math.sqrt(16))  # Square root

import pandas as pd
import numpy as np

# Example with pandas
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)
print(df)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file. And I am learning python and SQL.\n")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
