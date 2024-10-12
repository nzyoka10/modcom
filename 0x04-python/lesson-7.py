# Python Functions

'''
    -> A function is a block of code which only runs when it is called.
    -> You can pass data, known as parameters, into a function.
    -> A function can return data as a result.
'''

# Creating a Function
# In Python a function is defined using the def keyword:

# Function hello
def hello():
    print("Hello, first function!")

# To call a function, use the function name followed by parenthesis:
# Calling function hello()
hello()

print("\n")
# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.

# Example 2
def my_function(name):
    # print(name + " Kenya")
    print("Hello " + name)

my_function("Eric")
my_function("Super Metro")

# Function to add two numbers
def add_nums(num1, num2, sum):
    sum = num1 + num2
    print(sum)

add_nums(2, 2)