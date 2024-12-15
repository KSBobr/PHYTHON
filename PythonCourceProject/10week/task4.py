# https://leetcode.com/problem-list/binary-tree/
# url:https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=problem-list-v2&envId=binary-tree


class Solution(object):
    def sumNumbers(self, root):
        def dfs(root, val):
            if not root:
                return 0
            val = val * 10 + root.val
            if root.left == root.right == None:
                return val
            return dfs(root.left, val) + dfs(root.right, val)

        return dfs(root, 0)
