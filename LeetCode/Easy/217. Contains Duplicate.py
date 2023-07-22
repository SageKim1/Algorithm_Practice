class Solution:
    # O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        # O(n)
        for num in nums:
            # O(1) | the lookup operation in a set => performed in constant time
            if num in seen:
                return True
            seen.add(num)
        return False
