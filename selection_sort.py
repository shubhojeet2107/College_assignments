def selection_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Iterate over each element in the array
    for i in range(n):
        # Assume the minimum is the current position
        min_idx = i
        
        # Check the rest of the array for a smaller element
        for j in range(i+1, n):
            # If a smaller element is found, update the index of the minimum element
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
