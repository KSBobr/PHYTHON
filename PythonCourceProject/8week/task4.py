# https://leetcode.com/problem-list/sliding-window/
# https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        M = {}
        ans = []
        ss = ""
        if len(s) < 10:
            return ans
        else:
            for i in range(10, len(s) + 1):
                ss = s[i - 10 : i]
                if ss in M:
                    M[ss] = 2
                else:
                    M[ss] = 1
            for ss in M:
                if M[ss] >= 2:
                    ans.append(ss)
            return ans
