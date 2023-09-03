def twoNumberSum(array, targetSum):
    # Brute Force
    # Time Complexity: O(N^2)
    # Space Complexity: O(1)
    
    for num in array:
        if (targetSum - num) in array and targetSum != num*2:
            return [num, targetSum - num]
    return []
