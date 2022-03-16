# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')
        def getSum(root: Optional[TreeNode]) -> int:
            nonlocal maxSum
            if root is None:
                return 0
            
            rightSum = max(getSum(root.right),0)
            leftSum = max(getSum(root.left),0)
            currentMax = rightSum + leftSum + root.val

            maxSum = max(maxSum, currentMax)

            return max(rightSum + root.val, leftSum + root.val)
        getSum(root)
        return maxSum