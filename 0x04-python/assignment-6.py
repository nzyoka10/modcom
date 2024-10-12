# Assignment 6

# Score grading
# 1 - 29 ---> Failed
# 30 - 49 --> Below average
# 50 - 69 --> Above average
# 70 - 100 --> Excellent

score = int(input("\n Enter mark score: "))

if score < 0 or score > 100:
    print("ERROR: Invalid input!!")
elif score <= 29:
    print("You Failed!")
elif score >= 30 and score <= 49:
    print("Below average")
elif score >= 50 and score <= 69:
    print("Above average")
elif score >= 70 and score <= 100:
    print("Excellent")


