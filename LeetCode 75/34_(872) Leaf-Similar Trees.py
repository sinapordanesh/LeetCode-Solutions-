# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def leaf_finder(self, root, results):
        if not root:
            return -1
        if self.leaf_finder(root.left, results) == -1 and not root.right:
            results.append(root.val)
        if self.leaf_finder(root.right, results) == -1 and not root.left:
            results.append(root.val)
        return results

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        results1 = []
        results2 = []

        results1 = self.leaf_finder(root1, results1)
        results2 = self.leaf_finder(root2, results2)

        if len(results1) == len(results2):
            for i in range(len(results1)):
                if results1[i] != results2[i]:
                    return False
        else:
            return False
        
        return True