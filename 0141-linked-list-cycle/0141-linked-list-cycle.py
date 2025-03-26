# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            if slow == fast:          # Cycle detected
                return True
        
        return False  # No cycle detected