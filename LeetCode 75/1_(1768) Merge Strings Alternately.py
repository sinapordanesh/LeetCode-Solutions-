class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)
        longer = max(word1, word2, key=len)
        wrange = len(longer)
        result = ""

        for i in range(wrange):
            if i < len1:
                result += word1[i]
            if i < len2:
                result += word2[i]

        
        return result
    