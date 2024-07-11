class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        slist = list(s)

        for i in range(1, len(slist)):
            if slist[i] == '*':
                j = i - 1
                while slist[j] == " ":
                    j -= 1
                slist[j] = " "
                slist[i] = " "
        
        result1 = "".join(slist)
        result2 = result1.replace(" ","")

        return result2