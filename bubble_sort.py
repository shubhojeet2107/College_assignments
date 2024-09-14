def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Track whether any swaps were made in this pass
        swapped = False
        
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swaps were made, the list is sorted
        if not swapped:
            break

# Example usage:
arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print("Sorted array:", arr)
