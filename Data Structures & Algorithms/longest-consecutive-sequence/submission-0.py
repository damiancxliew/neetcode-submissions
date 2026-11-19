class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        curr_max = 0
        nums.sort()
        for num in nums:
            dp[num] = dp.get(num-1, 0) + 1
            curr_max = max(curr_max, dp[num])
        return curr_max
