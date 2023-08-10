class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(min(n, m))
    def lengthOfLongestSubstring(self, input_str: str) -> int:
        total_len = len(input_str)
        max_len = 0
        char_idx_map = {}
        start_idx = 0

        for end_idx in range(total_len):
            if input_str[end_idx] in char_idx_map:
                start_idx = max(char_idx_map[input_str[end_idx]], start_idx)
            
            max_len = max(max_len, end_idx - start_idx + 1)
            char_idx_map[input_str[end_idx]] = end_idx + 1
        
        return max_len
