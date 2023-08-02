class Solution:
    # (The overall) Time Complexity: O(n)
    #   n = the number of elements in the 'nums' list
    # Space Complexity : O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # slicing the 'nums' list twice
        #   each slicing operation takes O(n) time
        # This creates two new lists in memory during the slicing operation
        #   These new lists are then used to overwrite the original 'nums' list.
        #   The space complexity is O(n) 
        #   because it depends on the size of the 'nums' list.
        nums[:] = nums[-k:] + nums[:-k]
