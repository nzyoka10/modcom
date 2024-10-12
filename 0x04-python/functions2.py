# ! 24/09/2024 - Python Functions
# Functions with parameters

# Example 1
def carDisplay(car):
    print("Car name: ", car)

# call the function and pass the argument
carDisplay("Toyota Supra")

# Example 2
def askHerName(name):
    print("Owner name: ", name)

# call the function
askHerName("Jayne")

# Example 3
def askHerNumber(number):
    print("Owner number: ", number)

# call the function
askHerNumber("911")

# Example 4
def ownerInfo(status, address):
    print("Status: ", status + "\n Address: ", address)

# call the function and pass the parameters
ownerInfo("Married", "Lukenya")

# Example 5
# visit and chocolate and dinner
def planVisit(place, gift, dinner):
    print("Place: ", place, "\n Gift: ", gift, "\nDinner: ", dinner)

# call function planVisit
planVisit("Lukenya", "Dark chocolate", "Chicken, Peas and Chapati")

# Example 6
def nextTime(meet):
    print("See you this weekend at ", meet)

# call the function
nextTime("21:00hrs")

print("\n")

# function to add two numbers
def add(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# call the function
add(2, 2)
add(8, 19)
add(346, 123)

# function to subtract
def diff(num1, num2):
    sum = num1 - num2
    print("Difference: ", sum)

# call the function
diff(14, 9)
diff(8, 19)
diff(34, 23)

# function to multiply 3 numbers
def multiply(num1, num2, num3):
    sum = num1 * num2 * num3
    print("Multiply: ", sum)

# call the function
multiply(2, 2, 2)
multiply(10, 5, 0)
multiply(5, 16, 67)

# function to divide 2 numbers
def divide(num1, num2):
    sum = num1 / num2
    print("Division: ", sum)

# call the function
divide(10, 5)
divide(13, 7)
divide(624, 12)

print("\n")

# Area of a circle (2*pi*radius)
def area_circle(radius):
    area = (2 * radius) * 3.14
    print("Area of Circle: ", area)

# call function
area_circle(14)
area_circle(21)
area_circle(10)

# Function to calculate interest
def total_interest(amount, rate, time):
    sum = amount * (rate/100) * time
    print("Total interest: ", sum)

# call function and pass arguments
total_interest(1000, 2, 4)
total_interest(50000, 12, 2)
total_interest(67600, 11, 3)

# Function to calculate BMI
# BMI is calculated by dividing an adult's weight in kilograms 
# by their height in metres squared.
def get_bmi(weight, height):
    sum = weight / (height * height)
    print("Your BMI: ", sum)

# call the function 
get_bmi(92, 1.6)
get_bmi(88, 2)

# if __name__ == "__main__":
#     add(12, 2)
