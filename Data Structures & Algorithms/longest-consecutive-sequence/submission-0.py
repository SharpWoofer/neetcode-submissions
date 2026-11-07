class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        longest_streak = 1
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                streak = 1
                while num + 1 in num_set:
                    streak += 1
                    num += 1
                longest_streak = max(longest_streak, streak)
        return longest_streak