class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        result = 0

        for center in range(2*n-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        
        return result
