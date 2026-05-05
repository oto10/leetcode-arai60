import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_scores = []

        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_scores, val)

        if len(self.top_k_scores) > self.k:
            heapq.heappop(self.top_k_scores)

        return self.top_k_scores[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
