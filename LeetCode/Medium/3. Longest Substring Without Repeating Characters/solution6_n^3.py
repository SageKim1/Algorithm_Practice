class Solution:
    # Time Complexity: O(n^3) -> Time Limit Exceeded
    # Space Complexity: O(min(n, m))
    # m : the size of the charset
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_len = 0

        def check_repeat_chars(start, end):
            char_exist = set()
            for i in range(start, end+1):
                if s[i] in char_exist:
                    return False
                char_exist.add(s[i])
            return True

        for i in range(length):
            for j in range(i, length):
                if check_repeat_chars(i, j):
                    max_len = max(max_len, j-i+1)
        
        return max_len
