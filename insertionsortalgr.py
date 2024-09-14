def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted into the sorted part
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Place the key in its correct position

    return arr

# The array to be sorted
arr = [45, 36, 15, 92, 35, 71, 64, 39, 73, 37]

# Sort the array
sorted_arr = insertion_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
