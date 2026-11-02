class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        # key: what's left, val: index
        for i in range(len(nums)):
            if nums[i] in mymap: return sorted([mymap[nums[i]], i])
            else: mymap[target - nums[i]] = i