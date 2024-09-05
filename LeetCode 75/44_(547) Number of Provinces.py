class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visitedCities = set()

        def visiting(city):
            visitedCities.add(city)
            for i in range(n):
                if i not in visitedCities and isConnected[city][i] == 1:
                    visiting(i)

        result = 0
        for j in range(n):
            if  j not in visitedCities:
                visiting(j)
                result += 1

        return result