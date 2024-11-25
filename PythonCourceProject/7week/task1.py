# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/permutation-in-string/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False
        h1 = 0
        for l in s1:
            h1 += ord(l) ** 2
        h2 = 0
        for i in range(len(s1)):
            h2 += ord(s2[i]) ** 2
        if h1 == h2:
            return True
        for i in range(len(s1), len(s2)):
            h2 = h2 - (ord(s2[i - len(s1)]) ** 2) + ord(s2[i]) ** 2
            if h1 == h2:
                return True
        return False
