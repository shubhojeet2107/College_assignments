def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted
    
    mid = len(arr) // 2  # Find the middle point to divide the array into two halves
    left_half = merge_sort(arr[:mid])  # Recursively sort the first half
    right_half = merge_sort(arr[mid:])  # Recursively sort the second half
    
    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    result = []  # This will hold the merged array
    i = j = 0  # Initialize pointers for left and right arrays
    
    while i < len(left) and j < len(right):  # Traverse both arrays
        if left[i] < right[j]:  # Compare elements from both arrays
            result.append(left[i])  # Append the smaller element to result
            i += 1  # Move the pointer in the left array
        else:
            result.append(right[j])  # Append the smaller element to result
            j += 1  # Move the pointer in the right array
    
    # Append any remaining elements from left or right arrays
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result  # Return the merged array
