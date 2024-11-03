def replace_numbers(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = 10
        else:
            numbers[i] = 5
    return numbers

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
updated_list = replace_numbers(numbers_list)
print("Updated list:", updated_list)