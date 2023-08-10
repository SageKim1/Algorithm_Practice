class Solution:
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        palindrome = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    palindrome.append(substr)

        return len(palindrome)
