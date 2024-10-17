"""https://leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/ugly-number-ii/"""


class Solution(object):
    def nthUglyNumber(self, n):
        Num = [0] * n
        Num[0] = 1
        i2, i3, i5 = 0, 0, 0
        next2, next3, next5 = 2, 3, 5

        for i in range(1, n):
            next = min(next2, next3, next5)
            Num[i] = next
            if next == next2:
                i2 += 1
                next2 = Num[i2] * 2
            if next == next3:
                i3 += 1
                next3 = Num[i3] * 3
            if next == next5:
                i5 += 1
                next5 = Num[i5] * 5

        return Num[-1]
