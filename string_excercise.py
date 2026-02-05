s = input("Enter a word: ").strip().lower()
rev = s[::-1]
if s == rev:
    print("It's a palindrome.")
else:
    print("It is not a palindrome.")
