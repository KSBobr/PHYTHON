"""
https://leetcode.com/problem-list/string/
url:https://leetcode.com/problems/bulls-and-cows/
"""

from typing import Counter


class Solution:
    def getHint(self, secret: str, guess: str):
        C = Counter(secret)
        b = 0
        c = 0
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s == g:
                b += 1
                if C[s]:
                    C[s] -= 1
                else:
                    c -= 1
            elif C[g]:
                c += 1
                C[g] -= 1
        ans = str(b) + "A" + str(c) + str("B")
        return ans
