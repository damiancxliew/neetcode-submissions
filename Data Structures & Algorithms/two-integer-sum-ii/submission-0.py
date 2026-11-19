class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(numbers)):
            num = numbers[i]
            temp = target - num
            if temp not in hashmap.keys():
                hashmap[num] = i + 1
            else:
                return [hashmap[temp], i + 1]
        
         
