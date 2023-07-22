class Solution:
    # O(n) | the number of elements in the input array 'nums'
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        suffix_product = [1] * n

        # O(n) | Iteration takes linear time
        prefix = 1
        for i in range(n):
            # operations such as multiplication and assignment -> constant time operations
            prefix_product[i] = prefix
            prefix *= nums[i]
        
        # O(n) | Iteration takes linear time
        suffix = 1
        for i in range(n-1, -1, -1):
            # operations such as multiplication and assignment -> constant time operations
            suffix_product[i] = suffix
            suffix *= nums[i]

        answer = [prefix_product[i] * suffix_product[i] for i in range(n)]
        return answer
