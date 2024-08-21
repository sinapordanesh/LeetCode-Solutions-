class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []     
        # while i < len(nums1) and j < len(nums2):
            
        #     while nums1[i] > nums2[j]:
        #             j += 1
        #             if j >= len(nums2): break
        #     if i >= len(nums1) or j >= len(nums2): break
        #     while nums1[i] < nums2[j]:
        #             i += 1
        #             if i >= len(nums1): break
        #     if i >= len(nums1) or j >= len(nums2): break
        #     if nums1[i] == nums2[j]:
        #         count1 = 0
        #         count2 = 0
        #         collision = nums1[i]
        #         while nums1[i] == collision:
        #             count1 += 1
        #             i += 1
        #             if i >= len(nums1): break 
        #         while nums2[j] == collision:
        #             count2 += 1
        #             j += 1
        #             if j >= len(nums2): break 
        #         if count1 == count2:
        #             repeating = count1
        #         else:
        #             repeating = min(count1, count2)
        #         for i in range(repeating):
        #             result.append(collision)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
                    
        return result

                