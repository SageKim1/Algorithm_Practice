class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    # The output array does not count as extra space for space complexity analysis
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        answer = [0]*length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i-1] * answer[i-1]
        
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
