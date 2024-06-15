class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowel = ['a', 'e', 'i', 'o', 'u']

        count = 0
        

        for i in range(k):
            if s[i] in vowel:
                count += 1

        if k == len(s):
            return count

        result = count
        for i in range(k, len(s)):
            if s[i] in vowel:
                count +=1 
            if s[i-k] in vowel:
                count -=1
            if count > result:
                result = count
        
        return result