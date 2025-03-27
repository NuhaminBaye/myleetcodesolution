class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Function to reverse a linked list from start to end
        def reverseLinkedList(start, end):
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev  # New head of the reversed list
        
        # Count the number of nodes in the linked list
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        dummy = ListNode(0)  # Dummy node to handle head easily
        dummy.next = head
        prev_group_end = dummy  # The end of the previous reversed group
        
        while count >= k:
            group_start = prev_group_end.next
            group_end = group_start
            
            # Move group_end to the end of the current group
            for _ in range(k - 1):
                group_end = group_end.next
            
            next_group_start = group_end.next  # Save the start of the next group
            
            # Reverse the current group
            new_group_start = reverseLinkedList(group_start, next_group_start)
            
            # Connect the previous group with the new reversed group
            prev_group_end.next = new_group_start
            
            # Connect the newly reversed group to the next group
            group_start.next = next_group_start
            
            # Move prev_group_end to the end of the newly reversed group
            prev_group_end = group_start
            
            # Decrease the count of remaining nodes
            count -= k
        
        return dummy.next  # Return the new head of the linked list

# Example usage:
def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating the linked list for the example [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.reverseKGroup(head, 2)

# Print the modified linked list
print_linked_list(new_head)  # Output: 2 -> 1 -> 4 -> 3 -> 5 -> None