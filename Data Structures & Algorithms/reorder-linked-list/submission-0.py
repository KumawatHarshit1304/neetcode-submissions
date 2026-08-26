# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Go to middle element
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # splitting into 2 ll
        first = head
        second = slow.next
        slow.next = None

        # reversing 2nd half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        second = prev

        # now merging 
        while second:
            # saves then update 
            first_next = first.next
            sec_next = second.next
            # update then move first and second
            first.next = second
            second.next = first_next

            first = first_next
            second = sec_next