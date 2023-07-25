class Solution:
    # Time Complexity: O(n) 
    # Space Complexity: O(1)
    # The solution modifies the input array 'nums' in-place and
    # doesn't use any additional space that scales with the size of the input.
    # It only uses a constant amount of extra space.
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # The soloution traverses the input array 'nums' once,
        # performing the operation of moving elements different from 'val' towards the front of the array.
        # The traversal and element-moving processes take O(n) time,
        # where n is the size of the 'nums' array.
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
