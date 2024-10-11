import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        result = r
        while l <= r:
            m = (l+r) // 2
            hours = 0
            for pile in piles: 
                hours += math.ceil(float(pile)/m)

            if hours <= h: 
                result = m
                r = m - 1
            else: 
                l = m + 1

        return result
