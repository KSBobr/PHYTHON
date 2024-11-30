# https://leetcode.com/problem-list/sliding-window/
# https://leetcode.com/problems/subarray-product-less-than-k/?envType=problem-list-v2&envId=sliding-window


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        su = 1
        ans = l = 0
        for r in range(len(nums)):
            su *= nums[r]
            while su >= k:
                su /= nums[l]
                l += 1
            if su < k:
                ans += r - l + 1
        return ans
