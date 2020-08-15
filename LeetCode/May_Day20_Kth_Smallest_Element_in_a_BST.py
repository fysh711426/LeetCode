# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def search(node):
            if node is None:
                return
            result = search(node.left)
            if result is not None:
                return result
            # 找到第 k 小的節點就返回
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            return search(node.right)
        return search(root)