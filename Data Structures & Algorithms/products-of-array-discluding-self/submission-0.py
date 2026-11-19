class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_multi = [1 for i in range(n)]
        postfix_multi = [1 for i in range(n)]
        prefix_multi[0] = nums[0]
        postfix_multi[-1] = nums[-1]
        for i in range(1, n):
            prefix_multi[i] = nums[i] * prefix_multi[i - 1]
            postfix_multi[-i-1] = nums[-i-1] * postfix_multi[-i]
        result = [1 for i in range(n)]
        for i in range(n):
            if i == 0:
                result[i] = postfix_multi[1]
            elif i == n - 1:
                result[i] = prefix_multi[i-1]
            else:
                result[i] = prefix_multi[i - 1] * postfix_multi[i + 1]
        return result
        
