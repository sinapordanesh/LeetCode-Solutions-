class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1: return 0
        if nums[n-1] > nums[n-2] : return n-1
            
        lo, hi = 0, n-1
        while lo <= hi: 
            m = (lo+hi)/2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]: return m
            elif nums[m-1] > nums[m]: hi = m
            elif nums[m+1] > nums[m]: lo = m+1