def display_words_with_hash(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()  # Split line into words
                formatted_line = '#'.join(words)  # Join words with '#'
                print(formatted_line)
    except FileNotFoundError:
        print("The file was not found.")

# Example usage
filename = "sample.txt"
display_words_with_hash(filename)
