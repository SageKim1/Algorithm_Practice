class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        longest = ""

        for char in s:
            if char not in longest:
                longest += char
            else:
                longest = longest[longest.index(char)+1:] + char
            
            if len(longest) > max_len:
                max_len = len(longest)
        
        return max_len
