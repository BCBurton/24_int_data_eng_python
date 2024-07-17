#SLIDE 9
#Total Votes Calculation:
#If votes_candidate_A = 1500 and votes_candidate_B = 1300, then the total votes can be calculated as:
#pythtotal_votes results in 2800
votes_candidate_A = 1500
votes_candidate_B = 1300
total_votes = votes_candidate_A + votes_candidate_B
print(total_votes)

#SLIDE 10
#total_registered_voters = 10000, voters_voted = 6000, and additional_votes_by_mail = 500
total_registered_voters = 10000
voters_voted = 6000
additional_votes_by_mail = 500
turnout_percentage = ((voters_voted + additional_votes_by_mail) / total_registered_voters) * 100
print(turnout_percentage)


#SLIDE 11
#Impact of Variable Modification
#Modifying a value in one variable can affect calculations involving other variables.

x = 10
y = 5
sum = x + y  # sum is 15
x = 20
sum = x + y  # sum is now 25
print(sum)

#SLIDE 12
#Initial Data Assignment
total_voters = 10000
voters_voted = 6000
mail_in_votes = 500
voters_voted = voters_voted + mail_in_votes  # voters_voted is now 6500
turnout_percentage = (voters_voted / total_voters) * 100  # turnout_percentage is now 65.0
print(turnout_percentage)


#Indexing Characters
#Characters in a string are identified by their index numbers, which can be positive or negative.
#Positive indexing starts at 0 from the beginning.
#Negative indexing starts at -1 from the end.

greeting = "Hello"
first_char = greeting[0]  # 'H'
last_char = greeting[-1]  # 'o'
print(first_char)
print(last_char)

#Concatenating Strings
#Combining first and last names:
first_name = "Jane"
last_name = "Smith"
full_name = first_name + " " + last_name  # "Jane Smith"
print(full_name)


#Slicing Strings
#Extracting the area code from a phone number:
phone_number = "123-456-7890"
area_code = phone_number[0:3]  # "123"
print(area_code)

#SLIDE 14
#Newline: "Hello\nWorld"
#Tab: "Hello\tWorld"
#Quote: "She said, \"Hello\""
varNewLine= "Hello\nWorld"
varTab= "Good bye\tMars"
varQuote= "She said, \"Laters\""
print(varNewLine+varTab+varQuote)

#SLIDE 17
# Voter Data Example
# Lists
# Storing names of registered voters:
# python
voters = ["John Doe", "Jane Smith", "Alice Brown"]
print(voters)

# Tuples
# Storing fixed coordinates of polling stations:
# python
station_coordinates = (40.7128, -74.0060)
print(station_coordinates)


# Dictionaries
# Storing voter information:
# python
voter_info = {"name": "John Doe", "age": 30, "city": "New York"}
print(voter_info)

# Sets
# Storing unique voter IDs:
# python
voter_ids = {101, 102, 103, 104}
print(voter_ids)

#SLIDE 18
# ELIF Statement
# Checks multiple conditions.
# Example:
# python
age = 20
if age >= 21:
    print("You can vote.")
elif age >= 18:
    print("You can pre-register to vote.")
else:
    print("You are too young to vote.")

# OR Operator
# Checks if at least one condition is true.
# Example:
# python

has_voter_id = False
has_proof_of_residency = True
if has_voter_id or has_proof_of_residency:
    print("Voter can proceed.")
