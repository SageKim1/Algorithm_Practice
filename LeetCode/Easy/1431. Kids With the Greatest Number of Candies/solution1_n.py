class Solution:
    # Time Complexity: O(n) = O(3n)
    # Space Complexity: O(n) = O(2n)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_origin = max(candies) # Time: O(n) | Space: O(1)
        candies_after = [candy + extraCandies for candy in candies] # Time: O(n) | Space: O(n)
        return [candy >= max_origin for candy in candies_after] # Time: O(n) | Space: O(n)
