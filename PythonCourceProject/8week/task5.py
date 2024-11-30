# https://leetcode.com/problem-list/sliding-window/
# https://leetcode.com/problems/find-k-closest-elements/?envType=problem-list-v2&envId=sliding-window


class Solution(object):
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - k

        while l < r:
            m = l + (r - l) // 2

            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l : l + k]
