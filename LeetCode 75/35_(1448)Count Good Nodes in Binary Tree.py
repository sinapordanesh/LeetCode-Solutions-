# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __init__(self):
        self.goods = 0 

    def node_search(self, root,road):
        if root:
            road.append(root.val)
            road.sort()
            if road[-1] == root.val:
                self.goods += 1
            
            self.node_search(root.left, road[:])
            self.node_search(root.right, road[:])

    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.goods = 0
        road = []
        self.node_search(root, road)

        return self.goods
        
    # Alternative solution, the recursive function is embeded onto the goodNodes
    # def goodNodes(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
        
    #     def dfs(node, curMax):
    #         if not node:
    #             return
    #         if node.val >= curMax:
    #             count[0] += 1
    #             curMax = node.val
    #         dfs(node.left, curMax)
    #         dfs(node.right, curMax)
        
    #     count = [0]
    #     dfs(root, root.val)
        
    #     return count[0]