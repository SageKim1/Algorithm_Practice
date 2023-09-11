def isValidSubsequence(array, sequence):
    # Write your code here.
    # # Time: O(N) | Space: O(1)
    for item in reversed(array): # Time: O(N) | N: length of array
        if len(sequence) == 0:
            return True
        if item == sequence[-1]:
            sequence.pop()
            
    return len(sequence) == 0
