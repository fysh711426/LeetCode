# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque([root])
        px, py = None, None
        while q:
            l = len(q)
            # 搜尋這層中的所有子節點
            for _ in range(l):
                n = q.popleft()
                for child in [n.left, n.right]:
                    if child == None:
                        continue
                    if child.val == x:
                        px = n.val
                    if child.val == y:
                        py = n.val
                    q.append(child)
            # 這層中有找到就離開
            if px or py:
                break
        return px and py and px != py