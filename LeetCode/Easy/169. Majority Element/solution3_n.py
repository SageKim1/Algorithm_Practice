class Solution:
    # Boyer-Moore Majority Vote Algorithm
    # -> Time Complexity: O(N), Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
