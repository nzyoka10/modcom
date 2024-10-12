# Program to calculate monthly nHIF contributions 
# based on user input gross salary

'''
    Premium rates
    Less than 5,999    -- 150.00
    6,000 - 7,999      -- 300.00
    8,000 - 11,999     -- 400.00
    12,000 - 14,999    -- 500.00
    15,000 - 19,999    -- 600.00
    20,000 - 24,999    -- 750.00
    25,000 - 29,999    -- 850.00
    30,000 - 49,999    -- 1,000.00
    50,000 - 99,999    -- 1,500.00
    Over 100,000       -- 2,000.00
'''

# User to enter gross salary (in Ksh)
gross_salary = float(input("\n Enter your gross salary (Ksh): "))

# Variable to hold the monthly contribution
monthly_contribution = 0

if gross_salary < 0:
    # less than Zero (0) or Negative value
    print("ERROR: Invalid amount!!")

elif gross_salary < 6000:
    # less than 5,999 Ksh
    monthly_contribution = 150

elif gross_salary < 8000:
    # between 6,000 and 7,999 Ksh
    monthly_contribution = 300

elif gross_salary < 12000:
    # between 8,000 and 11,999 Ksh
    monthly_contribution = 400

elif gross_salary < 15000:
    # between 12,000 and 14,999 Ksh
    monthly_contribution = 500

elif gross_salary < 20000:
    # between 15,000 and 19,999 Ksh
    monthly_contribution = 600

elif gross_salary < 25000:
    # between 20,000 and 24,999 Ksh
    monthly_contribution = 750

elif gross_salary < 30000:
    # between 25,000 and 29,999 Ksh
    monthly_contribution = 850

elif gross_salary < 50000:
    # between 30,000 and 49,999 Ksh
    monthly_contribution = 1000

elif gross_salary < 100000:
    # between 50,000 and 99,999 Ksh
    monthly_contribution = 1500
else:
    # over 100,000 Ksh
    monthly_contribution = 2000

# Output
print("|-----------------------------|")
print("|          Salary Report        |")
print("|-------------------------------|")
print("| Gross Salary: Ksh", gross_salary)
print("| nHIF Contribution: Ksh", monthly_contribution)
print("|_______________________________|")

