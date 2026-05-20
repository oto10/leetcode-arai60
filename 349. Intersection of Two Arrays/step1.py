from collections import defaultdict

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_to_exists = defaultdict(int)
        for num1 in nums1:
            num1_to_exists[num1] = 1

        intersections = set()
        for num2 in nums2:
            if num1_to_exists[num2] == 1:
                intersections.add(num2)

        return list(intersections)
