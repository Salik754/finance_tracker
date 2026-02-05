# TASK: Write a program that reverses a word input by the user.

# Prompt the user to enter a word
user_input = input("Enter a word: ").strip()
# Reverse the word using slicing
reversed_word = user_input[::-1]
# Display the reversed word
print(f"The reversed word is: {reversed_word}")
