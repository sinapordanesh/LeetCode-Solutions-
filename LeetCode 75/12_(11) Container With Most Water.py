class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 0:
            return 0

        maximum, i, j = 0, 0, len(height)-1

        while (i < j):
            if height[i] <= height[j]:
                calc = height[i] * (j-i)
                i += 1
            else:
                calc = height[j] * (j-i)
                j -= 1

            if calc > maximum: maximum = calc
        
        return maximum 
        