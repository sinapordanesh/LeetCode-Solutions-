def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        print(len(flowerbed))
        
        for i in range(len(flowerbed)):
                         
            if i == 0:
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
    
    
array = [1,0,0,0,0,1]
canPlaceFlowers(array, 2)