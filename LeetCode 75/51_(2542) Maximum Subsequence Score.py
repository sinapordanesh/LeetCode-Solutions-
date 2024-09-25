import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        # pairs = list(zip(nums1, nums2))
        # pairs.sort(key=lambda x: x[1], reverse=True)

        sum_nums1 = 0
        max_score = 0
        min_heap = []

        for num1, num2 in sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True):
            heapq.heappush(min_heap, num1)
            sum_nums1 += num1

            if len(min_heap) > k: 
                sum_nums1 -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                max_score = max(max_score, sum_nums1*num2)
        
        return max_score