class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N) = O(2N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for char in word1:
            res += char
            if word2 != "":
                res += word2[0]
                word2 = word2[1:]
        if word1 != "":
            res += word2
        return res
