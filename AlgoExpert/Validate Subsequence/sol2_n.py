def isValidSubsequence(array, sequence):
    # One Pointer
    # Time: O(N) | N: length of array
    # Space: O(1)
    ptr = 0
    for item in array:
        if ptr == len(sequence):
            return True
        if item == sequence[ptr]:
            ptr += 1

    return ptr == len(sequence)
