"""
Username Creator

This script asks the user for their name and age.
It will format the name and check to see if the age is valid
Then, it will print a message to the screen
"""


def format_username(name: str) -> str:
    """Formats the username into a simple ussername"""

    # Clean the name by removing spaces
    clean_name = name.strip()

    # Convert name to lowercase
    clean_name = clean_name.lower()

    # Replace spaces with underscores
    username = clean_name.replace(" ", "_")

    # Return the formatted username
    return username


def get_age() -> int:
    """Asks the user for their age and validates it"""
    try:
        # Ask the user for their age
        age_input = input("Please enter your age: ")

        # Convert the input to an integer
        age = int(age_input)

        # Return valid age
        return age

    # If the conversation fails or age is invalid...
    except ValueError:
        # Print a nice message
        print("Invalid age input. Please enter a valid integer.")
        # Return -1 to signal an error
        return -1


def main() -> None:
    """Main program logic."""
    # ask user for their name
    name = input("Please enter your name: ")

    # call the format_username function to create a username
    username = format_username(name)

    # ask user for their age
    age = get_age()

    # if age is vaild
    if age != -1:
        # print a message to the user
        print(f"Hello {username}! You are {age} years old.")

    # if age is not valid
    else:
        print(f"Hello {username}! Your age is invalid.")


if (    
    __name__ == "__main__"
):  # Make sure the code doesn't run if imported BY SOMEONE ELSE
    main()
