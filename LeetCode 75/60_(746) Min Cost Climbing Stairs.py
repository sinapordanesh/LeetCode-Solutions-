class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        steps = [0] * len(cost)
        steps[0] = cost[0]
        steps[1] = cost[1]

        for i in range(2, len(cost)):
            steps[i] = cost[i] + min(steps[i-1], steps[i-2]) 

        return min(steps[-1], steps[-2])