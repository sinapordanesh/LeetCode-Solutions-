class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = ['a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E']
        char_list = list(s)
        r = ''

        size = len(char_list)
        for i in range(size):
            if char_list[i] in vowels:
                for j in range(i+1, size):
                    if char_list[j] in vowels:
                        r = char_list[j]
                        char_list[j] = char_list[i]
                        char_list[i] = r
                        i = j
                        break

        result = ''.join(char_list)
        return result