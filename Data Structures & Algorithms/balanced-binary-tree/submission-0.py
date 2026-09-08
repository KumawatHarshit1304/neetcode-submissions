# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # check whether node exists
            if node is None:
                return True,0
            leftBal,leftH = dfs(node.left)
            rightBal,rightH = dfs(node.right)

            balanced = (leftBal
             and rightBal 
             and abs(leftH - rightH)<=1)

            height = 1 + max(leftH,rightH)

            return balanced,height

        balanced,height = dfs(root)
        return balanced

        
        