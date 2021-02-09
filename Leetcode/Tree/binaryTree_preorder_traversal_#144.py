# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# 时间复杂度：O(n)，n为节点数，访问每个节点恰好一次。
# 空间复杂度：空间复杂度：O(h)，h为树的高度。最坏情况下需要空间O(n)，平均情况为O(logn)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def preOrder(root):
            if not root:
                return False
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return res