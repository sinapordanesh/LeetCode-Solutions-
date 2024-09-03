# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: 
            return root

        curr = root
        prev = root

        while curr and curr.val != key: 
            prev = curr
            if key < curr.val:
                curr = curr.left
            else: 
                curr =  curr.right
        if not curr or not prev: 
            return root

        if curr.right != None:
            if curr.left != None:
                right = None
                rnext = curr.right
                left = curr.left
                while rnext != None:
                    right = rnext
                    rnext = rnext.left
                if key == prev.left.val:
                    prev.left = curr.right
                else:
                    prev.right = curr.right
                right.left = left 
            else:
                if key == prev.left.val:
                    prev.left = curr.right
                else:
                    prev.right = curr.right
        elif curr.left != None:
            if key == prev.left.val:
                prev.left = curr.left
            else:
                prev.right = curr.left
        else:
            if key == prev.left.val:
                prev.left = None
            else:
                prev.right = None


        return root