# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def takeCharacters(self, s, k):
        n = len(s)
        l, r = 0, 0
        ans = n
        a, b, c = 0, 0, 0
        TA, TB, TC = s.count("a"), s.count("b"), s.count("c")
        if TA < k or TB < k or TC < k:
            return -1
        while r < n:
            if s[r] == "a":
                a += 1
            elif s[r] == "b":
                b += 1
            else:
                c += 1
            r += 1
            while a > TA - k or b > TB - k or c > TC - k:
                if s[l] == "a":
                    a -= 1
                elif s[l] == "b":
                    b -= 1
                else:
                    c -= 1
                l += 1
            ans = min(ans, n - (r - l))

        return ans
