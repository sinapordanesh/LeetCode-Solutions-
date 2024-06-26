class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        freq1 = [0] * 26
        freq2 = [0] * 26
        set1 = set()
        set2 = set()

        for c in word1:
            freq1[ord(c) - ord('a')] += 1 
            set1.add(c)
        for c in word2:
            freq2[ord(c) - ord('a')] += 1 
            set2.add(c)

        freq1.sort()
        freq2.sort()

        return freq1 == freq2 and set1 == set2