class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited = set()
        visited.add((0, 0))
        candidate_heap = [(nums1[0] + nums2[0], 0, 0)]
        k_pairs_with_smallest_sums = []

        def push_heap(x, y):
            if x < len(nums1) and y < len(nums2) and (x, y) not in visited:
                visited.add((x, y))
                heapq.heappush(candidate_heap, (nums1[x] + nums2[y], x, y))

        while len(k_pairs_with_smallest_sums) < k:
            _, i, j = heapq.heappop(candidate_heap)
            k_pairs_with_smallest_sums.append([nums1[i], nums2[j]])
            push_heap(i + 1, j)
            push_heap(i, j + 1)

        return k_pairs_with_smallest_sums
