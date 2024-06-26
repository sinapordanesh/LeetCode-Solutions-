class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()

        hmap = {}
        first = arr[0]
        occurance = 0
        for i in arr:
            if i == first:
                occurance += 1
            else:
                hmap[occurance] = 1
                occurance = 1
                first = i
        hmap[occurance] = 1

        if len(hmap) != len(set(arr)):
            return False
        else:
            return True