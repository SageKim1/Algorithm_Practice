def twoNumberSum(array, targetSum):
    # Two Pointers
    # Time Complexity: O(N logN)
    # Space Complexity: O(1)

    # .sort()
    # - an instance method (built-in method) for Python's list objects
    # - sorts the original list in-place
    # - doesn't return a sorted copy
    
    # sorted(my_list)
    # - a built-in function in Python (a function that is part of the core Python language)
    # - doesn't modify the original list
    # - returns a new list that contains the sorted elements

    # Timsort algorithm : combination of (Insertion Sort & Merge Sort)
    # Time: O(N logN) | Space: O(N)
    array.sort()
    left_ptr = 0
    right_ptr = len(array) - 1

    while left_ptr < right_ptr:
        currentSum = array[left_ptr] + array[right_ptr]
        if currentSum == targetSum:
            return [array[left_ptr], array[right_ptr]]
        elif currentSum < targetSum:
            left_ptr += 1
        elif currentSum > targetSum:
            right_ptr -= 1

    return []
