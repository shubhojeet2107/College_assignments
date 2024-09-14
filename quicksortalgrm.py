def quick_sort(arr):
    # Base case: if the array is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (here we choose the last element)
    pivot = arr[-1]
    
    # Create two sub-arrays: one for elements less than the pivot and one for elements greater than the pivot
    less_than_pivot = []
    greater_than_pivot = []
    
    # Partition the array into the two sub-arrays
    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            less_than_pivot.append(arr[i])
        else:
            greater_than_pivot.append(arr[i])
    
    # Recursively apply quick_sort to the sub-arrays and combine them with the pivot
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# The array to be sorted
arr = [45, 36, 15, 92, 35, 71, 64, 39, 73, 37]

# Sort the array
sorted_arr = quick_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
