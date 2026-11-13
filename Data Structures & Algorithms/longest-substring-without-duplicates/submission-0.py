class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        L, longest = 0,0
        seen = set()
        seen.add(s[0])
        for R in range(1, len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            longest = max(longest, len(seen))
        return longest