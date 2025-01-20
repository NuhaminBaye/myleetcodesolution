# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Move fast pointer two steps and slow pointer one step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches the end, slow will be at the middle
        return slow

# Example usage:
# Create a linked list for testing: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
middle = solution.middleNode(head)

# Print the values from the middle node to the end
result = []
while middle:
    result.append(middle.val)
    middle = middle.next

print(result)  # Output: [3, 4, 5]