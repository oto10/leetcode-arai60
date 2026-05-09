class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited_indices = set()
        visited_indices.add((0, 0))
        min_candidates = [(nums1[0] + nums2[0], 0, 0)]
        k_pairs_with_smallest_sums = []

        def add_candidate(x, y):
            if x < len(nums1) and y < len(nums2) and (x, y) not in visited_indices:
                visited_indices.add((x, y))
                heapq.heappush(min_candidates, (nums1[x] + nums2[y], x, y))

        while len(k_pairs_with_smallest_sums) < k:
            _, i, j = heapq.heappop(min_candidates)
            k_pairs_with_smallest_sums.append([nums1[i], nums2[j]])
            add_candidate(i, j + 1)
            add_candidate(i + 1, j)

        return k_pairs_with_smallest_sums
