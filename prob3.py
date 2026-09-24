# PROBLEM 3
#SCHOOL GRADE LEVEL VALIDATOR


valid_grade = (7,8,9,10,11,12)
try:
    grade = int(input("Bro, what's your grade level??? "))
    if grade in valid_grade:
        print("Valid Grade Level")
    else:
        print("Invalid Grade Level")
except ValueError:
    print("Invalid, enter a whole number")

