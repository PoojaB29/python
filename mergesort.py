#Written by Pooja
#On 14 Oct 2020
""" Question :
Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        #get middle element
        s = head
        f = head.next
        while (f is not None and f.next is not None):
            s = s.next
            f = f.next.next
        l = head
        r = s.next
        s.next = None
        l = self.sortList(l)
        r = self.sortList(r)
        return self.merge(l,r)
    
    def merge(self, L, R) -> ListNode:
        if(L == None):
            return R
        if (R == None):
            return L
        h = None
        if (L.val <= R.val):
            h = L
            h.next = self.merge(L.next, R)
        else:
            h = R
            h.next = self.merge(L, R.next)
        return h
        