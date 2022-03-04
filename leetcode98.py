# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Bless this mess
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root.left:
            if root.left.val >= root.val:
                return False
            elif not self.isValidLeft(root, root.left):
                return False
            
        if root.right:
            if root.right.val <= root.val:
                return False
            elif not self.isValidRight( root, root.right):
                return False
        return True
        
    def isValidRight(self, lowestValue: TreeNode, root: TreeNode) -> bool:
        if root.left:
            if root.left.val >= root.val or root.left.val <= lowestValue.val:
                return False
            elif not self.isValidLeft(root, root.left):
                return False
            
        if root.right:
            if root.right.val <= root.val:
                return False
            elif not self.isValidLeft( root, root.left):
                return False
        return True
        
        
    def isValidLeft(self,lowestValue: TreeNode, root: TreeNode) -> bool:
        if root.left:
            if root.left.val >= root.val:
                return False
            elif not self.isValidLeft(root, root.left):
                return False
            
        if root.right:
            if root.right.val <= root.val or root.right.val >= lowestValue.val:
                return False
            elif not self.isValidLeft(root, root.left):
                return False
        return True

#Better solution
def isValidBST(self, root, left = float('-inf'), right = float('inf')):
        return not root or left < root.val < right and \
                self.isValidBST(root.left, left, root.val) and \
                self.isValidBST(root.right, root.val, right)