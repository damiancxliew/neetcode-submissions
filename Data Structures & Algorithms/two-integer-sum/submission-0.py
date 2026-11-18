class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(nums)):
            num = nums[i]
            temp = target - num
            if temp in dic:
                return [dic[temp], i]
            dic[num] = i
        