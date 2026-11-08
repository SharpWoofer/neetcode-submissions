from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        para_dict = {}
        para_dict['('] = ')'
        para_dict['{'] = '}'
        para_dict['['] = ']'
        myStack = deque()
        for char in s:
            if char in para_dict.keys(): myStack.append(char)
            else:
                if not myStack: return False
                curr = myStack.pop()
                if char != para_dict[curr]: return False
        if not myStack: return True
        else: return False