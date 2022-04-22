# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = []
        levelNodes = [root]
        while root and levelNodes:
            currentNodes = []
            nextLevelNodes = []
            for node in levelNodes:
                currentNodes.append(node.val)
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)
            results.append(currentNodes)
            levelNodes = nextLevelNodes
        return results