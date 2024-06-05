class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        clean_s = ' '.join(s.split())
        
        s_array = clean_s.split()
        result = ""

        for i in range(len(s_array) - 1, -1, -1):
            if i != 0:
                result = result + s_array[i] + " "
            else:
                result = result + s_array[i]

        return result