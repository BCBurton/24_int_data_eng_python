import pandas as pd
#SERIES SECTION 
# What is a Series?
# "A Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floats, etc.). It is similar to a column in a DataFrame or a list in Python, but with additional capabilities and methods for data manipulation."

# Key Features of a Series
# Labeled Index: Each element in a Series is associated with a label, which allows for more intuitive data access and manipulation.
# Homogeneous Data: Unlike DataFrames, Series can only hold data of a single type.

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print("Series from list:\n", s)

# Creating a Series with custom index
s_custom_index = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with custom index:\n", s_custom_index)

# Accessing elements in a Series
print("\nFirst element in Series:", s[0])
print("Element with index 'c':", s_custom_index['c'])

# Performing operations on a Series
print("\nSeries after adding 5:\n", s + 5)

# Creating a Series from a dictionary
data_dict = {'x': 100, 'y': 200, 'z': 300}
s_dict = pd.Series(data_dict)
print("\nSeries from dictionary:\n", s_dict)


#DATA FRAME SECTION
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Ismael'],
    'Age': [24, 27, 22, 32,0],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston','Houston']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:\n", df)

# Accessing a column
print("\nNames:\n", df['Name'])

# Accessing multiple columns
print("\nNames and Ages:\n", df[['Name', 'Age']])

# Filtering data
print("\nPeople older than 25:\n", df[df['Age'] > 25])

# Adding a new column
#TRY ADDIN ANOTHER NUMBER AT THE END, WHAT HAPPENS?
df['Salary'] = [70000, 80000, 50000, 120000, 100]
print("\nDataFrame with Salary:\n", df)

# Grouping data
print("\nAverage Age by City:\n", df.groupby('City')['Age'].mean())
