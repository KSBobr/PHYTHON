"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/?envType=problem-list-v2&envId=string
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        j = 0
        direction = -1
        for char in s:
            rows[j] += char
            if j == 0 or j == numRows - 1:
                direction *= -1
            j += direction
        return "".join(rows)
