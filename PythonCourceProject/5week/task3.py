"""https://leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/rabbits-in-forest/"""

import collections


class Solution(object):
    def numRabbits(self, answers):
        A = collections.Counter()
        ans = 0
        for x in answers:
            if A[x] % (x + 1) == 0:
                ans += x + 1
            A[x] += 1
        return ans
