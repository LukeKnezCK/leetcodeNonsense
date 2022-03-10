# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level = [root]
        pendulum = False
        while level and root:
            currentNodes = []
            nextLevel = []
            if pendulum:
                x = len(level)-1
                pendulum = False
                while x >= 0:
                    currentNodes.append(level[x].val)
                    if level[x].left:
                        nextLevel.insert(0,level[x].left)
                        if level[x].right:
                            nextLevel.insert(1,level[x].right)
                    elif level[x].right:
                        nextLevel.insert(0,level[x].right)
                    x-=1
            else:
                pendulum = True
                for y in level:
                    currentNodes.append(y.val)
                    if y.left:
                        nextLevel.append(y.left)
                    if y.right:
                        nextLevel.append(y.right)
            level = nextLevel
            result.append(currentNodes)
        return result