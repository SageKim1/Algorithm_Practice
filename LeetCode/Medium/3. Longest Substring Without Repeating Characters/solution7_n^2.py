class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_len = 1 if length > 0 else 0

        for i in range(length):
            seen = set()
            seen.add(s[i])
            for j in range(i+1, length):
                if s[j] in seen:
                    #max_len = max(max_len, j-i)
                    break
                seen.add(s[j])
                max_len = max(max_len, j-i+1)
        
        return max_len
