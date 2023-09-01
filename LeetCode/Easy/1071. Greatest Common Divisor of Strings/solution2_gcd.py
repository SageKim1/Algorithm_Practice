class Solution:
    # Greatest Common Divisor
    # Time Complexity: O(m+n)
    # Space Complexity: O(m+n)
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # Time: O(m+n)
            return ""
        
        # calculate the GCD using binary Euclidean algorithm
        max_length = gcd(len(str1), len(str2)) # Time: log(m*n)
        return str1[:max_length]
