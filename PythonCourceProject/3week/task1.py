"""https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game-ii/?envType=problem-list-v2&envId=array"""


class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        ans = 0
        while i < j:
            ans = max(ans, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans