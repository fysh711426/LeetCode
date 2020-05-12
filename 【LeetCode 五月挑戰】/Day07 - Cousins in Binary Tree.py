# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xNode = self.find(root, x)
        yNode = self.find(root, y)

        if xNode[0] == yNode[0] and xNode[1] != yNode[1]:
            return True
        return False
    
    # return (deep, parent)
    def find(self, root, val, deep=0, parent=None):
        if root is None:
            return None
        
        if root.val == val:
            return (deep, parent)
        
        nodes = [root.left, root.right]
        for node in nodes:
            result = self.find(node, val, deep + 1, root.val)
            if result is not None:
                return result