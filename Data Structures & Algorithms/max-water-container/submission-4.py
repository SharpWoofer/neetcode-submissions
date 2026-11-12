class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2: return 0
        L, R = 0, len(heights)-1
        maxArea = 0
        while L < R:
            maxArea = max(min(heights[L], heights[R]) * (R-L), maxArea)

            if heights[L] < heights[R]: L += 1
            elif heights[R] <= heights[L]: R -= 1
            
        return maxArea