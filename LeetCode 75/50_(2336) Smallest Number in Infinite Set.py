class SmallestInfiniteSet(object):

    def __init__(self):
        self.curr = 1
        self.set = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if self.set:
            mini = min(self.set)
            self.set.remove(mini)
            return mini
        else:
            self.curr += 1
            return self.curr - 1
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.curr:
            self.set.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)