# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        self.result = 0
        self.targetSum = targetSum
        # node_map = []

        def recursive(root, nodemap):
            if not root:
                return
            nodemap.append(root.val)
            
            temp = 0
            for i in range(len(nodemap) - 1, -1, -1):
                temp += nodemap[i]
                if temp == self.targetSum:
                    self.result += 1
            recursive(root.left, nodemap[:])
            recursive(root.right, nodemap[:])

        recursive(root, [])

        return self.result
        
        