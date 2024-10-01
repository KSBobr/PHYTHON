"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/next-permutation/
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        c = i - 1
        while nums[j] <= nums[c]:
            j -= 1
        nums[c], nums[j] = nums[j], nums[c]
        l, r = c + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
