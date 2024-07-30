# Loop
for i in range(5):
    print(i)

# >>>Function Definition
#"Functions help us modularize our code. Here's how to define and call a function:"
def greet(name,Age):
    return f"Hello! My name is {name}! \nI am {Age} years old."

# Function Call
print(greet("Brian", "30"))

# #"Modules allow us to use code written by others. For instance, we can use the math module for advanced mathematical operations:"
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

for i in range(4):
    print(f"Hello! My name is {df.Name[i]}. I am {df.Age[i]} years old.")

for i in range(4):
    print(greet(df.Name[i],df.Age[i]))
    if df.Age[i]==min(df.Age):
        print("I am the youngest!")
    elif df.Age[i]==max(df.Age):
        print("I am the oldest!")
    else:
        print("I am a middle child!")