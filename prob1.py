# Problem 1: Student Age Validator
age_input = input("What is your age? ")
try:
    # Converts the input into an integer
    age = int(age_input)

    # Check if age is within the valid range
    if 12 <= age <= 18:
        print("Valid age.")
    else:
        print("Invalid age. Age must be from 12 to 18.")

except ValueError:
    # Runs if integer conversion fails
    print("Invalid input. Please enter a whole number.")