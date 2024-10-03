class Solution(object):

    """
        Recursive version of BS
    """
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """

        potions.sort()
        result = []

        def bs(lo, hi, s):
            if lo >= hi:
                return None

            m = (hi+lo)//2
            prod = spells[s] * potions[m]
            if prod >= success and (m == 0 or spells[s] * potions[m - 1] < success):
                return m
            elif prod >= success:
                return bs(lo, m, s)
            else:
                return bs(m+1, hi, s)
            
            return None

        for i in range(len(spells)):
            lo, hi = 0, len(potions)
            mid = bs(lo, hi, i) 
            if mid is not None: 
                result.append(len(potions)-mid)
            else:
                result.append(0)

        return result  

    """
        While loop version BS
    """
    # def successfulPairs(self, spells, potions, success):
    #     n, m = len(spells), len(potions)
    #     potions.sort()
    #     res = [0] * n
    #     for i, s in enumerate(spells):
    #         l, r = 0, m - 1
    #         while l <= r:
    #             mid = (l + r) // 2
    #             if potions[mid] * s >= success:
    #                 res[i] += r - mid + 1
    #                 r = mid - 1
    #             else:
    #                 l = mid + 1
    #     return res         