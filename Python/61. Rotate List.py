# -- 61. Rotate List --
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases: empty list or single node
        if head is None or head.next is None:
            return head
      
        # Count the total number of nodes in the linked list
        current = head
        list_length = 0
        while current:
            list_length += 1
            current = current.next
      
        # Optimize k by taking modulo with list length to avoid unnecessary rotations
        k = k % list_length
      
        # If k is 0, no rotation needed
        if k == 0:
            return head
      
        # Use two pointers approach to find the rotation point
        # Move fast pointer k steps ahead
        fast_pointer = head
        slow_pointer = head
        for _ in range(k):
            fast_pointer = fast_pointer.next
      
        # Move both pointers until fast reaches the last node
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
      
        # Perform the rotation:
        # The new head is the node after slow_pointer
        new_head = slow_pointer.next
        # Break the link at the rotation point
        slow_pointer.next = None
        # Connect the original tail to the original head
        fast_pointer.next = head
      
        return new_head
