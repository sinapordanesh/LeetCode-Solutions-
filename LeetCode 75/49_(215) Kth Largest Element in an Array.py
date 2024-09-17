class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()

        if len(nums) == 1: 
            return nums[0]

        k_cal = 0
        maxi = 0
        for i in range(len(nums)-1, -1, -1):
            maxi = nums[i]
            k_cal += 1
            if k_cal == k: break   
        
        return maxi