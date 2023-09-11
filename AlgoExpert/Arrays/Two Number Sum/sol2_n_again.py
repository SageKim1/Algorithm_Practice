def twoNumberSum(array, targetSum):
    # Hash Table | Hash Map | Dictionary | Set
    # Time Complexity: O(N)
    # Space Complexity: O(N)

    '''
    my_set = set()
    for num in array:
        if targetSum - num in my_set and targetSum != num*2:
            return [num, targetSum - num]
        if num not in my_set:
            my_set.add(num)
    return []
    '''

    my_dict = {} # my_dict = dict()
    for num in array:
        if targetSum != num*2 and targetSum - num in my_dict:
            return [num, targetSum - num]
        if num not in my_dict:
            my_dict[num] = True
    return []
