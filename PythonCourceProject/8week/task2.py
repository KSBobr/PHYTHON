# https://leetcode.com/problem-list/sliding-window/
# https://leetcode.com/problems/sliding-window-maximum/submissions/1466529583/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        d = deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += (i,)
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += (nums[d[0]],)
        return out
