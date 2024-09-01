# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.result = []

        def search(root):
            if not root:
                return None
            self.result.append(root.val)
            search(root.left)
            search(root.right)
            
        while root.val != val: 
            if val < root.val:
                root = root.left
            else:
                root = root.right
        search(root)

        return self.result