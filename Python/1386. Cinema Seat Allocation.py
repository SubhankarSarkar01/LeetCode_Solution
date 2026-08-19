from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_by_row = defaultdict(int)
        for row, seat in reservedSeats:
            reserved_by_row[row] |= 1 << (10 - seat)
      
        family_group_masks = (0b0111100000, 0b0000011110, 0b0001111000)
      

        total_families = (n - len(reserved_by_row)) * 2
      
        # Check each row with reservations
        for row_reservation in reserved_by_row.values():
            # Try to place family groups in this row
            for mask in family_group_masks:
                # Check if this group position has no conflicts with reserved seats
                if (row_reservation & mask) == 0:
                    # Mark these seats as occupied and count the family
                    row_reservation |= mask
                    total_families += 1
      
        return total_families
