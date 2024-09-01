# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.result = []
        self.max_right_level = -1

        def search(root, level):
            if not root:
                return
            if level > self.max_right_level: 
                self.result.append(root.val)
                self.max_right_level += 1
            
            search(root.right, level+1)
            search(root.left, level+1)

        search(root, 0)
        return self.result
    