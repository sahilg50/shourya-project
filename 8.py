import csv

def create_csv_file(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['UserID', 'Password'])  # Write header
        
        while True:
            user_id = input("Enter User ID (or 'exit' to stop): ")
            if user_id.lower() == 'exit':
                break
            password = input("Enter Password: ")
            writer.writerow([user_id, password])  # Write user ID and password

def search_password(filename, user_id):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == user_id:
                    return row[1]  # Return the password if user ID matches
        return "User ID not found."
    except FileNotFoundError:
        return "CSV file not found."

# Example usage
filename = "user_data.csv"
create_csv_file(filename)

user_id_to_search = input("Enter User ID to search for password: ")
password = search_password(filename, user_id_to_search)
print("Password:", password)
