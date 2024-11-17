# https://leetcode.com/problem-list/sliding-window/
# url: https://leetcode.com/problems/maximum-length-of-repeated-subarray/?envType=problem-list-v2&envId=sliding-window
class Solution(object):
    def findLength(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        ans = 0
        DP = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                else:
                    DP[i][j] = 0
                ans = max(ans, DP[i][j])
        return ans
