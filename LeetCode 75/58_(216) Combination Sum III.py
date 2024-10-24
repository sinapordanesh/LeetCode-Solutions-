class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        def summing(dig_list, curr, target):
            for i, c in enumerate(dig_list):
                summ = sum(curr) + c
                if summ == target: 
                    if len(curr) + 1 == k:
                        results.append(curr + [c])
                        break
                elif summ < target:
                    if len(curr) + 1 < k and len(dig_list) != 1:
                        summing(dig_list[i+1:], curr + [c], target)
                else: return
            return

        starting = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        current = []

        summing(starting, current, n)

        return results