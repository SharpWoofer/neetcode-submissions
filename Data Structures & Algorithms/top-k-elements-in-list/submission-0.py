from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mymap = defaultdict(int)
        for num in nums:
            mymap[num] += 1

        bucket_arr = [[] for i in range(len(nums) + 1)]
        for num, count in mymap.items():
            bucket_arr[count].append(num)
        
        res = []
        for i in range(len(bucket_arr) -1, 0, -1):
            for num in bucket_arr[i]:
                res.append(num)
                if len(res) == k: return res