"""https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/valid-sudoku/"""


class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a != ".":
                    res += [(i, a), (a, j), (i // 3, j // 3, a)]
        return len(res) == len(set(res))
