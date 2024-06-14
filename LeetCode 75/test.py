def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """


        avg = 0
        initial_avg = 0

        for i in range(k):
            avg += nums[i]

        if k == len(nums):
            return  avg/k

        tail = nums[0]
        temp = avg
        
        for j in range(k, len(nums)):
            print(j)
            temp = temp - tail + nums[j]
            tail = nums[j-k+1]
            if temp > avg:
                avg = temp 
        print(avg/k)
        return avg/k
    
i = [1,12,-5,-6,50,3]
k = 4
findMaxAverage(i, k)