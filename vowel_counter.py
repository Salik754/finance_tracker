# TASK: Create a program that counts the number of vowels in a word.

# Prompt the user to enter a string
user_input = input("Enter a word: ").strip().lower()
# Define a string containing all vowels
vowels = "aeiou"
# Initialize a counter to zero
count = 0
# Iterate over each character in the string
for char in user_input:
    if char in vowels:
        count += 1
# If the character is a vowel, increment the counter
# Display the total number of vowels found
print(f"The number of vowels in the given word is: {count}")
