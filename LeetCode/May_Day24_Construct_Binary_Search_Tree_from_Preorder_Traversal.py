# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def bst(nums):
            if not nums:
                return None

            val = nums[0]
            left  = [n for n in nums if n < val]
            right = [n for n in nums if n > val]

            node = TreeNode(val)
            node.left  = bst(left)
            node.right = bst(right)

            return node
        return bst(preorder)