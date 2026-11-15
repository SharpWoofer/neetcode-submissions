from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_map = defaultdict(int)
        for char in t:
            count_map[char] += 1
        
        res = ""
        res_len = float('inf')
        L = 0
        have = 0
        need = len(count_map)
        window = defaultdict(int)
        for R in range(len(s)):
            window[s[R]] += 1
            if s[R] in count_map:
                if window[s[R]] == count_map[s[R]]:
                    have += 1
                    
                    while have == need:
                        if R - L + 1 < res_len:
                            res_len = R - L + 1
                            res = s[L:R+1]
                        
                        window[s[L]] -= 1
                        if s[L] in count_map:
                            if window[s[L]] < count_map[s[L]]:
                                have -= 1
                        L += 1
        return res if res_len != float('inf') else ""