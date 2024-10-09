"""https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum-closest/"""


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]
                if abs(Sum - target) < abs(ans - target):
                    ans = Sum
                if Sum > target:
                    k -= 1
                elif Sum < target:
                    j += 1
                else:
                    return target
        return ans
