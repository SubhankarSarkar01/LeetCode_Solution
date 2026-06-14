class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Store all node values in a list
        values = []
      
        # Traverse the linked list and collect all values
        current = head
        while current:
            values.append(current.val)
            current = current.next
      
        # Get the total number of nodes
        n = len(values)
        max_twin_sum = max(values[i] + values[n - 1 - i] for i in range(n // 2))
      
        return max_twin_sum
