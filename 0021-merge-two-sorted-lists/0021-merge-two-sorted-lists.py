class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode()
        current = dummy
        
        # Iterate while both lists have nodes
        while list1 and list2:
            # Compare the values of the nodes from each list
            if list1.val < list2.val:
                current.next = list1  # Append the smaller node
                list1 = list1.next    # Move to the next node in list1
            else:
                current.next = list2  # Append the smaller node
                list2 = list2.next    # Move to the next node in list2
            
            current = current.next  # Move to the last node in the merged list
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list, which starts at dummy.next
        return dummy.next