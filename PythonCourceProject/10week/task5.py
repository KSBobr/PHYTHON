# https://leetcode.com/problem-list/binary-tree/
# https://leetcode.com/problems/path-sum-ii/?envType=problem-list-v2&envId=binary-tree


class Solution:
    def pathSum(self, root, targetSum):
        def pathSum(root, lst):
            if not root:
                return
            if root.left == root.right:
                if sum(lst) + root.val == targetSum:
                    ans.append(lst + [root.val])
                return

            if root.left:
                pathSum(root.left, lst + [root.val])
            if root.right:
                pathSum(root.right, lst + [root.val])

        ans = []
        pathSum(root, [])
        return ans
