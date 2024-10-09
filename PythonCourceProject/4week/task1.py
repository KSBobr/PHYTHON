"""https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/h-index/?envType=problem-list-v2&envId=array"""


class Solution(object):
    def hIndex(self, citations):
        H = 0
        citations.sort()
        n = len(citations)
        l, r = 0, n + 1
        while l < r:
            m = (r + l) // 2
            h = 0
            for i in range(n):
                if m <= citations[i]:
                    h += 1
                if h >= m:
                    break
            if h >= m:
                H = m
                l = m + 1
            else:
                r = m
        return H
