class Solution:
    # Two Pointers
    # Time Complexity: O(N) = O(2N)
    # Space Complexity: O(N) = O(2N)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1) # Time: O(1) | Space: O(1)
        len2 = len(word2) # Time: O(1) | Space: O(1)
        ptr1, ptr2 = 0, 0 # Time: O(1) | Space: O(1)
        res = [] # Space: O(N) = O(2N)

        while ptr1 < len1  or ptr2 < len2: # Time: O(2N)
            if ptr1 < len1:
                res += word1[ptr1]
                ptr1 += 1
            if ptr2 < len2:
                res += word2[ptr2]
                ptr2 += 1
        
        # list -> str | Time: O(N)
        return "".join(res)
