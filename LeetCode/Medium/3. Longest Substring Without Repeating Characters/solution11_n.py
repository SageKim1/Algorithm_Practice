class Solution:
    # int[128] for ASCII
    # Time Complexity: O(n)
    # Space Complexity: O(m), O(1)
    # m: the size of the charset
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_indices = [None] * 128 # list
        left_idx = right_idx = 0
        max_len = 0

        while right_idx < len(s):
            right_char = s[right_idx]

            prev_idx = char_indices[ord(right_char)]
            if prev_idx is not None and left_idx <= prev_idx < right_idx:
                left_idx = prev_idx + 1
            
            max_len = max(max_len, right_idx - left_idx+ 1)

            char_indices[ord(right_char)] = right_idx
            right_idx += 1
        
        return max_len
