# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maximum = -100000
        self.sums = [0] * 1
        result = 0

        def searcher(root, curlevel):
            if not root:
                return
            if curlevel >= len(self.sums) and curlevel != 0:
                self.sums.append(root.val)
            else:
                self.sums[curlevel] += root.val
            
            searcher(root.left, curlevel+1)
            searcher(root.right, curlevel+1)

        searcher(root, 0)

        for i in range(len(self.sums)):
            if self.sums[i] > maximum:
                result = i
                maximum = self.sums[i]
        
        return result+1 