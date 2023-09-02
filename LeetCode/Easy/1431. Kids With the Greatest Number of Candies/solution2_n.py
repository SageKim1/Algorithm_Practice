class Solution:
    # Time Complexity: O(n) = O(2n)
    # Space Complexity: O(n)
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_origin = max(candies) # Time: O(n) | Space: O(1)
        result = []

        # Time: O(n) | Space: O(n)
        for candy in candies:
            result.append(candy + extraCandies >= max_origin)

        return result
