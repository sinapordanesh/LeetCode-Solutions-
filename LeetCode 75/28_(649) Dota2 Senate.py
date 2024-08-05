class Solution(object):
    
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """ 
        senate = list(senate)
        R, D = deque(), deque()

        for i, c in enumerate(senate):
            if c == "R": 
                R.append(i)
            else:
                D.append(i)
                
        while D and R:
            r = R.popleft()
            d = D.popleft()
            
            if r < d: 
                R.append(r + len(senate))
            else:
                D.append(r + len(senate))

        return "Radiant" if R else "Dire"
        

