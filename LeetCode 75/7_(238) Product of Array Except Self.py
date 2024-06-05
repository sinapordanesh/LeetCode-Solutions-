class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1] * length

        left = [1] * length
        right = [1] * length

        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            left[i] *= right 
            right *= nums[i]

        # for i in range(length):
        #     result[i] = right[i] * left[i]
        
        return left