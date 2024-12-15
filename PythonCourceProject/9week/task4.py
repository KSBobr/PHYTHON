# https://leetcode.com/problem-list/binary-tree/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1479562446/?envType=problem-list-v2&envId=binary-tree


class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        root = TreeNode(preorder.pop(0))  # type: ignore
        root_idx = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx + 1 :])
        return root
