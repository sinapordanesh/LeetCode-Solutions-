class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n, l, max_w, zeros = len(nums), 0, 0, 0

        for r in range(n):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
                
            w = r - l + 1
            max_w = max(max_w, w)

        return max_w
            

