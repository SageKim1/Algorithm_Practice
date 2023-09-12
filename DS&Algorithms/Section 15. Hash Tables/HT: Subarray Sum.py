# WRITE SUBARRAY_SUM FUNCTION HERE #
def subarray_sum(nums, target):
    sum_idx = {0:-1}
    current_sum = 0
    
    for index, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_idx:
            return [sum_idx[current_sum-target] + 1, index]
        else:
            sum_idx[current_sum] = index
    
    return []
####################################




nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
