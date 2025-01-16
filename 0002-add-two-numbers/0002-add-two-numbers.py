# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
          # Initialize the dummy head of the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the current values (0 if the list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node with the digit
            
            # Move to the next nodes in the lists
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next of dummy head which points to the actual result
        return dummy_head.next