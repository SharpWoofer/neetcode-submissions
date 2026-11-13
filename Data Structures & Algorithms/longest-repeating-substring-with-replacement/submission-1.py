from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2: return len(s)
        L, length = 0, 1
        seen = defaultdict(int)
        seen[s[L]] = 1
        max_frequency = 1
        for R in range(1, len(s)):
            seen[s[R]] += 1
            max_frequency = max(seen[s[R]], max_frequency)
            if (R - L + 1) - max_frequency > k:
                seen[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length