# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        s = set()
        n = len(nums)
        su = 0
        ans = 0
        j = 0

        for i in range(n):
            while nums[i] in s:
                su -= nums[j]
                s.remove(nums[j])
                j += 1

            s.add(nums[i])
            su += nums[i]

            if len(s) == k:
                ans = max(ans, su)
                su -= nums[j]
                s.remove(nums[j])
                j += 1

        return ans
