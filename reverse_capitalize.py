# TASK: Write a function that reverses a word and capitalizes it.


# Define a function that takes a string parameter
def reverse_and_capitalize(word):
    # Create an empty string to store the reversed word
    reversed_word = ""
    # Loop through each character in the word
    for char in word:
        # Add each character to the front of the new string
        reversed_word = char + reversed_word
    # Convert the reversed word to uppercase
    return reversed_word.upper()


# Prompt the user for input and call the function
user_input = input("Enter a word: ")
result = reverse_and_capitalize(user_input)
# Display the transformed word
print(f"The reversed and capitalized word is: {result}")
