"""Given a binary tree, determine if it is height-balanced. Returns result in O(n)"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def helperDFS(root):
            if not root:
                return [True, 0]
            left = helperDFS(root.left)
            right = helperDFS(root.right)
            diff = abs(left[1] - right[1])
            is_balanced = left[0] and right[0] and diff <= 1
            return [is_balanced, 1 + max(left[1], right[1])]

        return helperDFS(root)[0]
