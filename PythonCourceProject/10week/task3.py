# https://leetcode.com/problem-list/binary-tree/
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?envType=problem-list-v2&envId=binary-tree


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
