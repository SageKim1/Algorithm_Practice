def isValidSubsequence(array, sequence):
    # Write your code here.
    # Time: O(N) | N: length of array
    # Space: O(1)
    for item in reversed(array):
        if len(sequence) == 0:
            return True
        if item == sequence[-1]:
            sequence.pop()
            
    return len(sequence) == 0
