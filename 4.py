def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        # Assume the minimum element is the current element
        min_index = i
        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the found minimum element with the current element
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

# Example usage
numbers_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(numbers_list)
print("Sorted list:", sorted_list)
