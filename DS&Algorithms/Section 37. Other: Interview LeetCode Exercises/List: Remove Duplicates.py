# WRITE REMOVE_DUPLICATES FUNCTION HERE #
def remove_duplicates(nums):
    idx = 0
    
    while idx+1 < len(nums):
        if nums[idx] == nums[idx+1]:
            nums.pop(idx+1)
        else:
            idx += 1
            
    return len(nums)
#########################################
    
    

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)
print("Unique values in list:", nums[:new_length])


"""
    EXPECTED OUTPUT:
    ----------------
    New length: 5
    Unique values in list: [0, 1, 2, 3, 4]

"""
