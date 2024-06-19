class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        num1_d = []
        num2_d = []
        result = []

        for num in nums1:
            if num not in nums2:
                if num not in num1_d:
                    num1_d.append(num)
        for num in nums2:
            if num not in nums1:
                if num not in num2_d:
                    num2_d.append(num)

        result.append(num1_d)
        result.append(num2_d)

        return result
