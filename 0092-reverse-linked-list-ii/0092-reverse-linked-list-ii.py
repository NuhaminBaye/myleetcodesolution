# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node before the `left` position
        for _ in range(left - 1):
            prev = prev.next
        
        # Start the reversal process
        reverse_start = prev.next
        curr = reverse_start.next
        
        # Reverse the sublist from left to right
        for _ in range(right - left):
            reverse_start.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = reverse_start.next
        
        return dummy.next