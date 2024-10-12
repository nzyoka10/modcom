# Wed :: 18/09/2024

# Introduction to python
# Variables - is a container used to store values

# Rules of naming Variable
# 1. Must Start with a Letter or Underscore
    # Example: my_variable, _temp, var1

# 2. Case Sensitive: Variable names are case sensitive, (myVariable, MyVariable, and MYVARIABLE)
    # Example: count, Count, COUNT

# 3. No Spaces: Variable names cannot contain spaces
    # Example: user_age is valid, while user age is not.

# 4. No Special Characters: Variable names cannot include special characters like @, #, $, %, etc. Only letters, numbers, and underscores are allowed.
    # Example: item_list is valid, while item$list is not.

# 5. Not to use python keywords
    # Example: global, else, print

# You should not start with a number
    # Eg:- 2age, 56fruits

# Variable Naming Convention
# 1. Snake case - words are delimited with an underscore (_)
    # Eg:- first_name, var_1, maize_price

# 2. Pascal case - words are delimited with a capital letter
    #  Eg:- FistName, StudentAge, MaizePrice 

# 3. Camel case - words are delimited with capital case except the initial word
    # Eg:- firstName, studentAge, maizePrice

# creating first variable
age = 56
print(age) 

# country
country = "Kenya"
print(country)

# send message
message = "Wake Up, Gym time"
print(message)

# print(age, country, message)
print("\n")
# Concatenation
age = 80
message = "Today is Monday"

print("Age is: ", age)
print("Message is: ", message)

print("My age is: " + str(age) + " and the message is: " + message)
