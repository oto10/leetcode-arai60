class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = dict()
        for num in nums:
            if num not in num_frequency:
                num_frequency[num] = 0

            num_frequency[num] += 1

        return sorted(num_frequency, key=num_frequency.get, reverse=True)[:k]
