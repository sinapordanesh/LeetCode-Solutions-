import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n = len(piles)

        if n == h: return max(piles)
        if n == 1: return math.ceil(n/h)
        ser_piles = [(x, 1) for x in piles]
        ser_piles = sorted(ser_piles, key=lambda x: x[0])
        j = h - n
        i = n-1
        while j != 0: 
            curr = ser_piles[i][0]
            b = ser_piles[i][1]
            ser_piles[i] = ((curr*b)//(b+1), b+1)
            j -= 1
            if ser_piles[i][0] >= ser_piles[i-1][0]: continue
            else: i -= 1

        return math.ceil(max(ser_piles, key=lambda x: x[0])[0])  
    