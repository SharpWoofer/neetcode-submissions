class Solution:

    def encode(self, strs: List[str]) -> str:
        # Multiple strings -> 1 string
        # [Length] + [Special Char] + [Actual String]
        oneString = ""
        for string in strs:
            oneString += f"{len(string)}#{string}"
        return oneString

    def decode(self, s: str) -> List[str]:
        res = []
        length = ''
        last_saved = 0
        i = 0
        while True:
            if i >= len(s): return res
            if s[i] == "#":
                length = int(s[last_saved:i])
                res.append(s[i+1: i+1+length])
                i,last_saved = i+1+length-1, i+1+length
            i += 1
