# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy  # This will point to the last node of the swapped pair
        current = head  # This will point to the current node to be swapped
        
        while current and current.next:
            # Nodes to be swapped
            first = current
            second = current.next
            
            # Perform the swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the pointers forward for the next pair
            prev = first
            current = first.next
        
        return dummy.next  # The new head of the modified list

# Example usage:
# You can create a linked list and call the swapPairs function like this:
def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating a linked list for testing: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

solution = Solution()
swapped_head = solution.swapPairs(head)

print_list(swapped_head)  # Output: 2 -> 1 -> 4 -> 3 -> None