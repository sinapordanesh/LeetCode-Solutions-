# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.paths = []

        def zigzog(root, roadsize, previous):
            if previous:
                roadsize += 1 
                if previous == 'l':
                    if root.right:
                        zigzog(root.right, roadsize, 'r')
                    else:
                        self.paths.append(roadsize-1)
                elif previous == 'r':
                    if root.left:
                        zigzog(root.left, roadsize, 'l')
                    else:
                        self.paths.append(roadsize-1)

            if root.right:
                zigzog(root.right, 1, 'r')
            if root.left:
                zigzog(root.left, 1, 'l')
        
        if root.left or root.right:
            zigzog(root, 0, None)
        else:
            return 0

        return max(self.paths)