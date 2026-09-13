# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0,True
            
            leftH,lbalanced = dfs(node.left)
            rightH,rbalanced = dfs(node.right)

            balanced = (
                lbalanced
                and rbalanced
                and abs(leftH-rightH)<2)
                
            return 1 + max(leftH,rightH),balanced
        
        height,bal = dfs(root)
        return bal
        