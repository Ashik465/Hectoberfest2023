def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping happens, the array is already sorted
        swapped = False

        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n - i - 1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

    return arr

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print("Sorted array:", sorted_list)
