"""https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/combination-sum/"""


class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        S = [(target, [], 0)]
        while S:
            t, combination, st = S.pop()
            if t < 0:
                continue
            if t == 0:
                ans.append(combination)
                continue
            for i in range(st, len(candidates)):
                S.append((t - candidates[i], combination + [candidates[i]], i))
        return ans
