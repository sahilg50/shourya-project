import pickle

# Function to create a binary file with names and roll numbers
def create_binary_file(filename):
    with open(filename, 'wb') as file:
        while True:
            name = input("Enter Name (or 'exit' to stop): ")
            if name.lower() == 'exit':
                break
            roll_number = input("Enter Roll Number: ")
            # Write name and roll number as a tuple
            pickle.dump((name, roll_number), file)

# Function to search for a roll number in the binary file
def search_roll_number(filename, roll_number_to_search):
    try:
        with open(filename, 'rb') as file:
            while True:
                try:
                    name, roll_number = pickle.load(file)
                    if roll_number == roll_number_to_search:
                        return name  # Return the name if roll number matches
                except EOFError:
                    break  # End of file reached
        return None  # Roll number not found
    except FileNotFoundError:
        return "Binary file not found."

# Example usage
filename = "student_data.dat"
create_binary_file(filename)

roll_number_to_search = input("Enter Roll Number to search for Name: ")
name_found = search_roll_number(filename, roll_number_to_search)

if name_found:
    print("Name:", name_found)
else:
    print("Roll number not found.")
