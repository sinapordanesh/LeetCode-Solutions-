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
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        maxim = 0
        while prev:
            maxim = max(maxim, head.val + prev.val)
            prev, head = prev.next,  head.next

        return maxim