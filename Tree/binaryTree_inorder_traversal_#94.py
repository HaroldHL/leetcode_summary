# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# 时间复杂度：O(n)，n为节点数，访问每个节点恰好一次。
# 空间复杂度：空间复杂度：O(h)，h为树的高度。最坏情况下需要空间O(n)，平均情况为O(logn)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return False
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res