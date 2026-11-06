class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixLtoR = []
        total = 1
        for num in nums:
            total = total * num
            prefixLtoR.append(total)
        total = 1
        prefixRtoL = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            total = total * nums[i]
            prefixRtoL[i] = total
        
        res = []
        total = 1
        for i in range(0, len(nums)):
            if i == 0: left = 1
            else: left = prefixLtoR[i-1]
            if i + 1 >= len(nums): right = 1
            else: right = prefixRtoL[i+1]
            res.append(left * right)

        return res