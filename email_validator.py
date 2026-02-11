# TASK: Write a function that validates an email format.


# Define a function that takes a string parameter
def valid_email(email):
    # Check if '@' is in the email
    if "@" not in email:
        return False
    # Extract the last four characters of the email
    last_four = email[-4:]
    # Check if it ends with '.com' or '.net'
    if last_four == ".com" or last_four == ".net" or last_four == "s.ca":
        return True
    else:
        return False


# Prompt the user for an email input and call the function
user_input = input("Enter an email address: ")
is_valid = valid_email(user_input)
# Display whether the email is valid
if is_valid:
    print("The email address is valid.")
else:
    print("The email address is not valid.")
