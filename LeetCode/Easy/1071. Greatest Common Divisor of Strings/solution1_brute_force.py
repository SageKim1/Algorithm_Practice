class Solution:
    # Brute Force
    # Time Complexity: O(min(m, n)*(m+n))
    # Space Complexity: O(min(m, n))
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k: # Time: O(1)
                return False
            n1, n2 = len1 // k, len2 // k # Time: O(1)
            base = str1[:k] # Time: O(k) | Space: O(min(m, n))
            return str1 == n1 * base and str2 == n2 * base # Time: O(m+n)

        # i: min(len1, len2) -> 1
        for i in range(min(len1, len2), 0, -1): # Time: O(min(m, n))
            if valid(i):
                return str1[:i]
        
        return ""
