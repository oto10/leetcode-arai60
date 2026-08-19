class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sum_to_count = {0: 1}
        for num in nums:
            current_sum += num
            count += prefix_sum_to_count.get(current_sum - k, 0)
            prefix_sum_to_count[current_sum] = prefix_sum_to_count.get(current_sum, 0) + 1

        return count
