def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Element found, return its index
        elif mid_value < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half

    return -1  # Element not found

# Example usage:
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_element = 12

result = binary_search(my_list, target_element)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
