def count_word_occurrences(filename, target_word):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire file
            words = content.split()  # Split the content into words
            count = words.count(target_word)  # Count occurrences of the target word
            return count
    except FileNotFoundError:
        return "The file was not found."

# Example usage
filename = "sample.txt"
target_word = "my"
occurrences = count_word_occurrences(filename, target_word)

if isinstance(occurrences, int):
    print(f"The word '{target_word}' occurs {occurrences} time(s) in the file '{filename}'.")
else:
    print(occurrences)
