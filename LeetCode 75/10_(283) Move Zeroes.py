class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        result = [0] * len(nums)

        i = 0

        for num in nums:
            if num != 0: 
                result[i] = num
                i += 1

        for j in range(len(result)):
            nums[j] = result[j]