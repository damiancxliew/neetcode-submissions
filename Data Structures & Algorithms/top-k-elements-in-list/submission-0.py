class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count = 0
        prev_num = None
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        res = []
        final = []
        for num in freq.keys():
            heapq.heappush(res, (-freq[num], num))
        for i in range(k):
            final.append(heapq.heappop(res)[1])
        return final

