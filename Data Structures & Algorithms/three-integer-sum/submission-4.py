class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        res = []
        for i in range(len(nums_sorted)):
            # Remove duplicates
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]: continue
            target = 0 - nums_sorted[i]
            L, R = i+1, len(nums_sorted)-1
            while L < R:
                if nums_sorted[L] + nums_sorted[R] < target: L += 1
                elif nums_sorted[L] + nums_sorted[R] > target: R -= 1
                elif nums_sorted[L] + nums_sorted[R] == target: 
                    res.append([nums_sorted[i], nums_sorted[L], nums_sorted[R]])
                    L += 1
                    R -= 1
                    # Remove duplicates
                    while L < R and nums_sorted[L] == nums_sorted[L-1]: L += 1
                    while L < R and nums_sorted[R] == nums_sorted[R+1]: R -= 1
        return res