# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0
    
    for num in nums:
        if num - 1 not in num_set:
            temp = num
            while temp+1 in num_set:
                temp += 1
            longest = max(longest, temp - num + 1)
    
    return longest
####################################################



print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
