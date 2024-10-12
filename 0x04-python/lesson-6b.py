# Lesson 6 --> 19/09/2024

# The if-elif-else Statement:
    # Checks multiple conditions in sequence and executes the
    #  corresponding block for the first true condition.

print("The if......elif....else Statement\n")

# ! Example 1
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# ! Example 2
# day = "Friday"
day = input("Please enter day of week: ").capitalize()

if day == "Monday":
    print("It's on a Monday")
elif day == "Tuesday":
    print("It's on a Tuesday")
elif day == "Wednesday":
    print("It's on a Wednesday")
elif day == "Thursday":
    print("It's on a Thursday")
elif day == "Friday":
    print("It's on a Friday")
elif day == "Saturday":
    print("It's on a Saturday")
elif day == "Sunday":
    print("It's on a Sunday")
else:
    print("Not day of the week!")

# ! Example 3
# User input for county name
county = input("Please enter county name: ").capitalize()

if county == "Nairobi":
    print("You selected Nairobi.")
elif county == "Mombasa":
    print("You selected Mombasa.")
elif county == "Kisumu":
    print("You selected Kisumu.")
elif county == "Nakuru":
    print("You selected Nakuru.")
elif county == "Makueni":
    print("You selected Makueni.")
elif county == "Meru":
    print("You selected Meru.")
elif county == "Machakos":
    print("You selected Machakos.")
elif county == "Kiambu":
    print("You selected Kiambu.")
elif county == "Nyeri":
    print("You selected Nyeri.")
elif county == "Uasin Gishu":
    print("You selected Uasin Gishu.")
else:
    print("ERROR: Not Found!!")

