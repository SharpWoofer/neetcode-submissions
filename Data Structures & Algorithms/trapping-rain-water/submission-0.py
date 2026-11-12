class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMaxLeft = [0] * len(height)
        maxL = 0
        for i in range(len(height)):
            if i == 0: prefixMaxLeft[i] = 0
            else:
                maxL = max(maxL, height[i-1])
                prefixMaxLeft[i] = maxL

        postfixMaxRight = [0] * len(height)
        maxR = 0
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1: postfixMaxRight[i] = 0
            else:
                maxR = max(maxR, height[i+1])
                postfixMaxRight[i] = maxR

        minLR = [0] * len(height)
        for i in range(len(height)):
            minLR[i] = min(prefixMaxLeft[i], postfixMaxRight[i])

        # calc = min(L, R) - height[i] (must be >= 0)
        res = 0
        for i in range(len(height)):
            calc = minLR[i] - height[i]
            if calc < 0: calc = 0
            res += calc
        
        return res