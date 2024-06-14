class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        result, num_map  = 0, Counter(nums)

        for value, count in num_map.items(): 
            pair_value = k - value
            if value < pair_value or pair_value not in num_map: continue
            result += min(count, num_map[pair_value]) if value != pair_value else count/2

        return result