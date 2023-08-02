class Solution:
    # Time complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        # O(n) | n = the number of elements in the input array 'nums'
        for i, num in enumerate(nums):
            complement = target - num
            # O(1) | Checking if an element exists in the dictionary
            if complement in num_dict:
                return [num_dict[complement], i]
            # O(1) | Adding an element to the dicionary
            num_dict[num] = i
