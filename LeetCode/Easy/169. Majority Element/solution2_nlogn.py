class Solution:
    # Time Complexity: O(N logN)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() # Time Complexity: O(N logN)
        if nums[0] == nums[len(nums)//2 + 1]:
            return nums[0]
        if nums[-1] == nums[len(nums)//2]:
            return nums[-1]
