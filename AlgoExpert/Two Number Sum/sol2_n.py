def twoNumberSum(array, targetSum):
    # Write your code here.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    my_set = set()
    for num in array:
        my_set.add(num)
        if targetSum != num*2 and (targetSum-num) in my_set:
            return [num, targetSum-num]
    return []
