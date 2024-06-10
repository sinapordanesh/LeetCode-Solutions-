class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len1 = len(s)
        len2 = len(t)

        i = 0
        j = 0

        if s == "":
            return True

        while  i < len1 and j < len2:
            temps = s[i]

            if temps == t[j]:
                if i == len1-1:
                    return True
                else:
                    i += 1
            j += 1

        return False
        