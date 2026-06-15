# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy_node = ListNode(next=head)

        slow_ptr = dummy_node
        fast_ptr = head
      
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
      
        # Delete the middle node by skipping it
        slow_ptr.next = slow_ptr.next.next
      
        # Return the head of the modified list
        return dummy_node.next
