"""https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game-ii/?envType=problem-list-v2&envId=array"""


class Solution:
    def jump(self, nums: List[int]) -> int:  # type: ignore
        i = 0
        n = len(nums)
        P = [10000] * n
        P[0] = 0
        while i < n:
            f = i + nums[i] + 1
            if f >= n:
                f = n
            for j in range(i + 1, f):
                P[j] = min(P[i] + 1, P[j])
            i += 1
        # print (P)
        return P[-1]
