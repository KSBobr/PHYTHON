# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/arithmetic-slices/?envType=problem-list-v2&envId=sliding-window


class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        ans = 0
        temp = 0
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                temp += 1
            else:
                temp = 0
            ans += temp
        return ans
