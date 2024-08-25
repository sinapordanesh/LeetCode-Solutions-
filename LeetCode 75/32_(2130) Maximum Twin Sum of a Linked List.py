# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        couner = head
        c = 0
        while counter.next:
            c += 1
            counter = counter.next

        halfnode = head
        for i in range(c/2):
            halfnode = halfnode.next
        
        current = halfnode.next.next
        previous = halfnode.next 

        while current:
            next = curret.next
            current.next = previous 
            previous = current 
            current = next

        halfnode.next = previous 

        start = head
        twin = halfnode.next
        maximum = start.val + twin.val
        for j in range(c/2):
            start = start.next
            twin = twin.next
            temp = start.val + twin.val
            if temp > maximun:
                maximun = temp

        return maximun