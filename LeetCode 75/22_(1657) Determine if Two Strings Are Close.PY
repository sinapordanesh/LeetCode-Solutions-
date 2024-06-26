class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        """
        SOLUTION IDEA
        For checking whether two words are eligible to execute both operations on them, there must be 2 conditions true about 2 words, which are:
            1. All characters on the word1 must be met on word2 as well (the use case of set())
            2. The general frequency of characters must be the same in both word1 and word2 (the use case of freq arrays). e.g. "aan" and "nan" have this condition, as both have the same frequency of characters (2 & 1). This is true for "rrtr" and "ttyt", althogh they dont have the first condition which we indicated above. 
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