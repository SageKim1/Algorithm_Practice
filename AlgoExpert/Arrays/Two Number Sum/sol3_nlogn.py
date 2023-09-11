def twoNumberSum(array, targetSum):
    # Write your code here.
    # Time Complexity: O(N logN)
    # Space Complexity: O(1)
    array.sort() # Quick Sort | Time: O(N logN) | Space: O(1)
    left_ptr = 0
    right_ptr = len(array) - 1

    while left_ptr < right_ptr: # Time: O(N)
        currentSum = array[left_ptr] + array[right_ptr]
        if currentSum == targetSum:
            return [array[left_ptr], array[right_ptr]]
        elif currentSum < targetSum:
            left_ptr += 1
        elif currentSum > targetSum:
            right_ptr -= 1
    return []
