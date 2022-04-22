# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            return self.symHelper(root.left, root.right)
        
    def symHelper(self, leftNode, rightNode) -> bool:
        if leftNode == None and rightNode == None:
            return True
        elif leftNode == None or rightNode == None:
            return False
        elif not leftNode.val == rightNode.val:
            return False
        else:
            return self.symHelper(leftNode.left, rightNode.right) and self.symHelper(leftNode.right, rightNode.left)