# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/maximum-erasure-value/?envType=problem-list-v2&envId=sliding-window
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        P = [-1] * 10001
        s = 0
        ans = 0
        l = 0
        for r, num in enumerate(nums):
            if P[num] >= l:
                s -= sum(nums[l : P[num] + 1])
                l = P[num] + 1
            s += num
            P[num] = r
            ans = max(ans, s)

        return ans
