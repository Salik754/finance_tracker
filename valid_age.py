# TASK: Write a function that asks for a valid age input and handles invalid inputs.


# Define a function that takes one string parameter
def get_valid_age(prompt):
    while True:
        # Ask the user for input using the prompt
        age_input = input(prompt)
        try:
            # Try to convert the input to an integer
            age = int(age_input)
            # Check if the number is positive
            if age > 0:
                return age
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")


# Create a loop that keeps asking for input until a valid age is entered

# Try to convert the input to an integer

# If successful, check if the number is positive

# If valid, return the number
# If not valid, show an error message and prompt again
# Call the function and store the result
# Display the valid age
age = get_valid_age("Enter your age: ")
print(f"Your valid age is: {age}")
