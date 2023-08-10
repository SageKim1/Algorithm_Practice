class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_len = 0
        seen = set()
        i = 0

        for j in range(length):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_len = max(max_len, j-i+1)

        return max_len
