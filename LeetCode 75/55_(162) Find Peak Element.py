class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
            
        lo, hi = 0, len(nums)-1
        while lo <= hi: 
            m = (lo+hi)/2
            if m == 0:
                if nums[m] > nums[m+1]:
                    return m
                else: 
                    lo = m+1
            elif m == len(nums) - 1:
                if nums[m] > nums[m-1]:
                    return m
                else: 
                    hi = m
            else:
                if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                    return m
                elif nums[m-1] > nums[m]:
                    hi = m
                elif nums[m+1] > nums[m]:
                    lo = m+1