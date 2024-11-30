# https://leetcode.com/problem-list/sliding-window/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        p = Counter(p)
        ans = []
        ss = None
        for i in range(0, n - m + 1):
            if i == 0:
                ss = Counter(s[:m])
            else:
                ss[s[i - 1]] -= 1
                ss[s[i + m - 1]] += 1
            if len(ss - p) == 0:
                ans.append(i)
        return ans
