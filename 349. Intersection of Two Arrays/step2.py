from bisect import bisect_left

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            small, large = nums1, sorted(nums2)
        else:
            small, large = nums2, sorted(nums1)

        intersections = set()
        for num in set(small):
            i = bisect_left(large, num)
            if i < len(large) and large[i] == num:
                intersections.add(num)

        return list(intersections)
