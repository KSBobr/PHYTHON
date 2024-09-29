"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/generate-parentheses/?envType=problem-list-v2&envId=string
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def DO(le, r, s):
            if len(s) == n * 2:
                ans.append(s)
                return

            if le < n:
                DO(le + 1, r, s + "(")

            if r < le:
                DO(le, r + 1, s + ")")

        ans = []
        DO(0, 0, "")
        return ans
