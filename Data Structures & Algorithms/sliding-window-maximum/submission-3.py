from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0: return [0]
        largest = -999
        count_map = defaultdict(int)
        res = []
        for i in range(0, k):
            largest = max(nums[i], largest)
            count_map[nums[i]] += 1
        res.append(largest)
        L = 0
        for R in range(k, len(nums)):
            count_map[nums[L]] -= 1
            if count_map[nums[L]] == 0:
                del count_map[nums[L]]
            L += 1
            count_map[nums[R]] += 1
            largest = max(count_map.keys())
            res.append(largest)
        return res