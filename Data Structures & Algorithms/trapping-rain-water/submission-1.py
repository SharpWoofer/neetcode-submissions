class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        maxLeft, maxRight = height[0], height[len(height)-1]
        res = 0
        while L < R:
            if maxLeft < maxRight:
                L += 1
                calc = min(maxLeft, maxRight) - height[L]
                if calc < 0: calc = 0
                maxLeft = max(maxLeft, height[L])
            else:
                R -= 1
                calc = min(maxLeft, maxRight) - height[R]
                if calc < 0: calc = 0
                maxRight = max(maxRight, height[R])
            res += calc
        return res