def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # If there are no words, return 0
    if not words:
        return 0

    # Find the last non-empty word
    last_word = words[-1]

    # Return the length of the last word
    return len(last_word)

# Example usage:
s =input( "Given a string s consisting of words and spaces -> ")
print(length_of_last_word(s))  # Output: 6
