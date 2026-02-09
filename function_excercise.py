# TASK: Write a function that returns a random encouragement message.

# Import the random module
import random

# Define a function with no parameters that returns a string


def get_encouragement():
    # Create four different message variables

    message1 = "You're doing great!"
    message2 = "Keep up the good work!"
    message3 = "You've got this!"
    message4 = "Believe in yourself!"

    # Generate a random number from 1 to 4

    random_number = random.randint(1, 4)

    # Use if-elif statements to return the corresponding message
    if random_number == 1:
        return message1
    elif random_number == 2:
        return message2
    elif random_number == 3:
        return message3
    else:
        return message4


# Call the function and print the result
print(get_encouragement())
