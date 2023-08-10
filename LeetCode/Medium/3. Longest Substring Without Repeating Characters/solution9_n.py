from collections import Counter
class Solution:
    # Time Complexity: O(n) = O(2n)
    # Space Complexity: O(min(n, m))
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_cnt = Counter()
        left = right = 0
        max_len = 0

        while right < len(s):
            char_right = s[right]
            char_cnt[char_right] += 1

            while char_cnt[char_right] > 1:
                char_left = s[left]
                char_cnt[char_left] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1
        
        return max_len
