# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
            
        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next
            
        # Remove the nth node from the end
        second.next = second.next.next
        
        # Return the modified list, starting from the next of dummy
        return dummy.next

# Example Usage
# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Helper function to convert linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
solution = Solution()

# Example 1
head1 = create_linked_list([1, 2, 3, 4, 5])
result1 = solution.removeNthFromEnd(head1, 2)
print(linked_list_to_list(result1))  # Output: [1, 2, 3, 5]

# Example 2
head2 = create_linked_list([1])
result2 = solution.removeNthFromEnd(head2, 1)
print(linked_list_to_list(result2))  # Output: []

# Example 3
head3 = create_linked_list([1, 2])
result3 = solution.removeNthFromEnd(head3, 1)
print(linked_list_to_list(result3))  # Output: [1]