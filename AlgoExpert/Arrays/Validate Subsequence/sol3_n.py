def isValidSubsequence(array, sequence):
    # Two Pointers
    # Time: O(N) | N: length of array
    # Space: O(1)
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)
