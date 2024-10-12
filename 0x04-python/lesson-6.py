# 19/09/2024

# Conditional Statements in Python
# They allow execution of certain blocks of code based on whether a 
# condition is true or false. 
# They enable decision-making in your programs.


# Three types of Conditional Statements:
# 1. The if Statement:-
    # Executes a block of code if the condition is true.
# Example 1
age = 10
if age < 18:
    print("Not eligible to vote!")

# Example 2
number = 20
if number > 0:
   print("POSITIVE NUMBER")

# Example 3 (Donate blood)
weight = 50
if weight >= 50:
   print("Donate blood, weight is okay, safe lives!")

# Example 4 (Military)
tattoo = False
if tattoo == False:
   print("Join the army!")

# Example 5 (Retirement)
emp_age = 66
if emp_age >= 65:
   print("Time to hang your boots!!")

# Example 6 (Marry)
marriage_age = 25
if marriage_age <= 29:
   print("Bro take your time, no rush!")


print("\n")
# 2. The if-else Statement:-
    # Executes one block of code if the condition is true, and another 
    # block if it is false.
# Example
temperature = 10
if temperature > 25:
    print("Hot day")
else:
    print("Cold day!")


print("\n")
# 3. The if-elif-else Statement:
    # Checks multiple conditions in sequence and executes the
    #  corresponding block for the first true condition.
# Example
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

print("\n")

# Python For Loop
    # A for loop is used to iterate over a sequence (like a list, tuple, string, or range) 
    # and execute a block of code for each item in the sequence.
# Syntax
    # for variable in sequence:
    # code block to execute
# Example 
fruits = ["Apple", "Banana", "Cherry", "Orange"]
for fruit in fruits:
    print(fruit)

# Python While Loop
    # A while loop repeatedly executes a block of code as long as a given condition is true.
    # Syntax
        # while condition:
        # code block to execute
# Example
count = 0
while count < 5:
    print(count)
    count += 1

print("\n")
print("break Statement")
# The break Statement
# With the break statement we can stop the loop even if 
    # the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("\n")
print("continue Statement")
# The continue Statement
#   With the continue statement we can stop the current iteration, 
#   and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)