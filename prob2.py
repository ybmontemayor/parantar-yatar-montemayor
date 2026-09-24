#Author - Aldrich John P. Parantar
#Date - 09/24/2026
#Purpose - To check if a username satisfies the given conditions and is valid.

#IMPORT RE TO ENABLE PATTERNS
import re

#INPUT - Asks the user to input their username.
username = input("Enter username: ")

#PATTERN - Pattern to be put into re function. "^" indicates string, [a-zA-Z0-9] excludes space and special characters, and {5,10} is the minimum and maximum number of characters.
pattern = r"^[a-zA-Z0-9]{5,10}$"

#SELECTION STRUCTURE - Checks if the username satisfies all conditions. Else. it is invalid.
if re.fullmatch(pattern, username):
    print("Valid username.")
else:
    print("Invalid username.")