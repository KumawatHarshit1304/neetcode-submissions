# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # middle element find kra
        s,f = head,head
        while f and f.next:
            s=s.next
            f=f.next.next
        # LL ko split kra
        first = head
        second = s.next
        s.next = None
        # 2nd half LL ko reverse kra
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        second = prev
        # ab merge krna h dono half ko
        while second:
            # next ko save kiya
            first_next = first.next
            sec_next = second.next
            # update kiya
            first.next = second
            second.next = first_next
            # pointer move kiya
            first = first_next
            second = sec_next



        