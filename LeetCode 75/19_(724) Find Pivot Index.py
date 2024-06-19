class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, sum(nums)
        n = len(nums)
        for i in range(n):
            right -= nums[i]
            if right == left:
                return i
            left += nums[i] 
        return - 1