class Solution:
    # Boyer-Moore Voting Algorithm
    # Time Complexity: The algorithm runs in linear time O(n),
    #                  where "n" is the size of the input array.
    # Space Complexity: The algorithm uses constant space O(1),
    #                   meaning the amount of extra memory it requires remains constant 
    #                   regardless of the input array's size.
    #                   It only uses a few variables to keep track of the count and the candidate element,
    #                   leading to a constant amount of memory usage.
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        # O(n) | It processes each element once.
        # the time it takes increases linearly with the size of the array.
        for num in nums:
            if count == 0:
                candidate = num
            
            count += 1 if num == candidate else -1
        
        return candidate
