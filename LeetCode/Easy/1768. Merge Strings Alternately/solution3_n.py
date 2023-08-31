class Solution:
    # One Pointer
    # Time Complexity: O(N)
    # Space Complexity: O(N) = O(2N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result= [] # Space: O(N)
        max_len = max(len(word1), len(word2)) # Time: O(1) | Space: O(1)

        for index in range(max_len): # Time: O(N) (N = max_len)
            if index < len(word1):
                result += word1[index]
            if index < len(word2):
                result += word2[index]
        
        return "".join(result)
