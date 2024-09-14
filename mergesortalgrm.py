def merge_sort(arr):
    # Base case: if the array has one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Recursively apply merge_sort to the two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    # Merge the two sorted arrays into one sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are any remaining elements in the left array, add them to the sorted array
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are any remaining elements in the right array, add them to the sorted array
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# The array to be sorted
arr = [45, 36, 15, 92, 35, 71, 64, 39, 73, 37]

# Sort the array
sorted_arr = merge_sort(arr)

# Print the sorted array
print("Sorted array:", sorted_arr)
