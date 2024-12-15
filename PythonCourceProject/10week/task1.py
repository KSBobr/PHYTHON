# https://leetcode.com/problem-list/binary-tree/
# https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=binary-tree


class Solution(object):
    def numTrees(self, n):
        A = [0] * (n + 1)
        A[0], A[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                A[i] += A[j] * A[i - j - 1]
        return A[-1]
