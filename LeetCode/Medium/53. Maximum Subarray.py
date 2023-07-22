class Solution:
    # Kadane's algorithm | to find the maximum subarray
    # O(n) | the overall time complexity of the solution
    # -> n represents the number of elements in the input array 'nums'
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here= max_so_far = nums[0]

        # it traverses the input array 'nums' once
        for num in nums[1:]:
            # O(1) | constant time
            # it calculates the maximum subarray ending at that index
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
