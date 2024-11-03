def find_vowels(input_string):
    vowels = "aeiouAEIOU"
    found_vowels = []
    for char in input_string:
        if char in vowels:
            found_vowels.append(char)
    
    # Remove duplicates
    found_vowels = list(set(found_vowels))
    return found_vowels

# Example usage
text = "Hello, how are you?"
vowels_in_text = find_vowels(text)
print("Vowels in the given string:", vowels_in_text)
