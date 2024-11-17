# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/submissions/1455593306/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def maxSubarrayLength(self, nums, k):
        ans = 0
        A = {}
        l = 0
        n = len(nums)
        for r in range(n):
            A[nums[r]] = A.get(nums[r], 0) + 1
            if A[nums[r]] > k:
                while nums[l] != nums[r]:
                    A[nums[l]] -= 1
                    l += 1
                A[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
