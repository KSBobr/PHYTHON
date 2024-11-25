# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def longestBeautifulSubstring(self, word):
        S = set()
        lo, ans = -1, 0
        for hi, c in enumerate(word):
            if hi > 0 and c < word[hi - 1]:
                S = set()
                lo = hi - 1
            S.add(c)
            if len(S) == 5:
                ans = max(ans, hi - lo)
        return ans
