"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head      #track which node we're on
        while current and current.next:     #checking for end of linked list
            if current.val == current.next.val:  #check for duplicate
                current.next = current.next.next  #excise duplicate node
            else:  #if else allows for removing multiple duplicates in a row before moving along
                current = current.next
        return head
