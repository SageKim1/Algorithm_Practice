class Solution:
    # "How should I handle duplicates?"
    # Questions about the order of inputs and outputs

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for element in nums1:
            if element in nums2:
                intersection.append(element)
        return intersection
