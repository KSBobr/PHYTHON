"""https://leetcode.com/problem-list/string/
https://leetcode.com/problems/count-and-say/"""


class Solution(object):
    def countAndSay(self, n):
        def NS(s):
            n = len(s)
            s = s
            c = 1
            news = ""
            if len(s) == 1:
                news = "1" + s
                return news
            else:
                s += "a"
                for i in range(1, n + 1):
                    if s[i - 1] == s[i]:
                        c += 1
                    else:
                        news += str(c) + str(s[i - 1])
                        c = 1
                return news

        st = "1"
        for i in range(1, n):
            st = NS(st)
            print(st)
        return st
