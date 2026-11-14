class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        count = [0] * 26
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            count[idx] += 1
        
        count2 = [0] * 26
        for i in range(0, len(s1)):
            idx = ord(s2[i]) - ord('a')
            count2[idx] += 1

        if count == count2: return True

        j = 0
        for i in range(len(s1), len(s2)):
            idx = ord(s2[j]) - ord('a')
            j += 1
            count2[idx] -= 1
            idx = ord(s2[i]) - ord('a')
            count2[idx] += 1
            if count == count2: return True
        return False