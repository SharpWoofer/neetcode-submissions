class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mymap = {}
        # key = tuple, val = strings
        count = [0] * 26
        for string in strs:
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            if tuple(count) not in mymap: mymap[tuple(count)] = [string]
            else: mymap[tuple(count)].append(string)
            count = [0] * 26
        for x in mymap.values(): res.append(x)
        return res