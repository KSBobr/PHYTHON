# https://leetcode.com/problem-list/sliding-window/
# url:https://leetcode.com/problems/minimum-size-subarray-sum/submissions/1455608257/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def minSubArrayLen(self, target, nums):
        i = 0
        j = 0
        s = 0
        mn = 10**10
        while j < len(nums):
            s += nums[j]
            while s >= target:
                s -= nums[i]
                mn = min(j - i + 1, mn)
                i += 1
            j += 1
        if mn == 10**10:
            return 0
        return mn
