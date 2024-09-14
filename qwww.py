def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    
    # Iterate over each position in the text where the pattern could fit
    for i in range(n - m + 1):
        j = 0
        # Check if the substring matches the pattern
        while j < m and text[i + j] == pattern[j]:
            j += 1
        # If j equals the length of the pattern, we found a match
        if j == m:
            return i  # Return the starting index of the match
    
    return -1  # Return -1 if no match is found

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = brute_force_string_match(text, pattern)
print("Pattern found at index:", result)
