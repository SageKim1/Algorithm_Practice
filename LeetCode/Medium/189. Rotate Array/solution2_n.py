class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums) # Time Complexity: O(1)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k] # Time Complexity: O(N)
