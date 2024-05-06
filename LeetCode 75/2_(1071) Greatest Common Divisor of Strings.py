class Solution(object):


    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        def compare_chars(str1, start, end, str2):

            substr1 = str1[start:end]

            if substr1 == str2:
                return True
            else:
                return False

        sizes = len(str1)
        sizet = len(str2)

        if (sizes % sizet != 0):
            return ""
        
        devisor = sizes/sizet

        pattern = True
        for i in range(devisor):
            if str1[i] == str2[i]:
                continue
            else:
                return ""

        for i in range(0, sizes-1, sizet):
            result = compare_chars(str1, i, i+sizet, str2)
            if result:
                continue
            else:
                return ""

        return str2     

        