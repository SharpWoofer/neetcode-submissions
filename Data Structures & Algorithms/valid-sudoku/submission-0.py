from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set) # k: (r/3, c/3)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if board[r][c] in cols[c]: return False
                else: cols[c].add(board[r][c])
                if board[r][c] in rows[r]: return False
                else: rows[r].add(board[r][c])
                if board[r][c] in boxes[(r//3, c//3)]: return False
                else: boxes[(r//3, c//3)].add(board[r][c])
        return True