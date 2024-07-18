#python basics
# >>>Variables and Data Types
a = 5  # Integer
b = 3.14  # Float
c = "Hello, LAST THING BEFORE I GO!"  # String
d = True  # Boolean
print(d)
print(c)

# >>>Basic Operations
sum = a + b  # Addition
difference = a - b  # Subtraction
product = a * b  # Multiplication
quotient = a / b  # Division
print(product)
print(quotient)

# >>>Control Structures
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Loop
for i in range(5):
    print(i)

# >>>Function Definition
#"Functions help us modularize our code. Here's how to define and call a function:"
def greet(name):
    return f"Hello, {name}!"

# Function Call
print(greet("Ismael"))

#"Modules allow us to use code written by others. For instance, we can use the math module for advanced mathematical operations:"
import math
print(math.sqrt(25))  # Square root

# >>> Pandas and Numpy
#"For data analysis, some key libraries we'll use are pandas and numpy:"
import pandas as pd
import numpy as np

# Example with pandas
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)
print(df)

# >>>File Handling and Basic I/O
#"Lastly, handling files is an essential skill. Here's a simple example of reading from and writing to a file:"
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


