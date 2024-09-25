class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        hmap = {nums2[i]: nums1[i] for i in range(len(nums1))}

        sorted_list = sorted(hmap.items(), key=lambda x: x[1], reverse=True)
        top_k = sorted_list[:k]

        product = 1
        for _, value in top_k:
            product += value

        min_num2 = min(key for key, _ in top_k)

        return product * min_num2

        