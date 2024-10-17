"""https://leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/sort-characters-by-frequency/"""


class Solution(object):
    def frequencySort(self, s):
        D = {}
        ans = ""
        for i in range(len(s)):
            if s[i] in D:
                D[s[i]] += 1
            else:
                D[s[i]] = 1
        Sor = sorted(D.items(), key=lambda x: x[1], reverse=True)
        print(Sor)
        for i in range(len(Sor)):
            ans += Sor[i][0] * Sor[i][1]
        return ans
