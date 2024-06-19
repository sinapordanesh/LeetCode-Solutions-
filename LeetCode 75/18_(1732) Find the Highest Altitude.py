class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_al, current = 0, 0
        for net in gain:
            current += net 
            max_al = max(max_al, current)
        return max_al
        