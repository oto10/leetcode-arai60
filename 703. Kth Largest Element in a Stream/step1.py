import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_k_scores = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.max_k_scores, val)

        if len(self.max_k_scores) > self.k:
            heapq.heappop(self.max_k_scores)

        return self.max_k_scores[0]


# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)
