class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        
        
        for i in range(len(flowerbed)): 
            
            if len(flowerbed)==1:
                if flowerbed[0]==0 and n==1:
                    return True
            elif i == 0 and len(flowerbed)>1:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -= 1    
            elif i == (len(flowerbed)-1):
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    n -= 1 
                    
            if n==0:
                return True
                
        return False
            