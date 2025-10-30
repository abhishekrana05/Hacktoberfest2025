# ------------------------------------------------------------
# Palindrome Checker with Sentence Support (Python)
# Description:
#   Checks whether a given sentence is a palindrome.
#   Ignores punctuation, spaces, and capitalization.
# Author: Abhishek Rana
# ------------------------------------------------------------

import re

def is_palindrome(text):
    """
    Function to check if a given text is a palindrome.
    Non-alphanumeric characters are ignored.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    # Compare cleaned string with its reverse
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_palindrome(sentence):
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")
