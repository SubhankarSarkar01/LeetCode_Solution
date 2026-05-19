class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize pointers for both arrays
        pointer1 = 0
        pointer2 = 0

        # Get the lengths of both arrays
        length1 = len(nums1)
        length2 = len(nums2)

        # Traverse both arrays using two pointers
        while pointer1 < length1 and pointer2 < length2:
            # If elements match, return the common element (minimum due to sorted order)
            if nums1[pointer1] == nums2[pointer2]:
                return nums1[pointer1]

            # Move the pointer pointing to the smaller element
            if nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1

        # No common element found
        return -1
