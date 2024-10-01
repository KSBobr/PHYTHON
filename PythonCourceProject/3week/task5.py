"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 2):
            ch1 = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                ch2 = nums[j]
                ch3 = nums[k]
                Sum = ch1 + ch2 + ch3
                if Sum > 0:
                    k -= 1
                elif Sum < 0:
                    j += 1
                else:
                    ans.add((ch1, ch2, ch3))
                    j += 1
                    k -= 1
        return ans
