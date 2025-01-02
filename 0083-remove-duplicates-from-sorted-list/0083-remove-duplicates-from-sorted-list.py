# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one element, return it as is
        if not head or not head.next:
            return head
        
        # Initialize the current node to the head of the list
        current = head
        
        # Traverse the linked list
        while current and current.next:
            # If the current node's value is the same as the next node's value
            if current.val == current.next.val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return head