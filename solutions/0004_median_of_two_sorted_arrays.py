class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # the shorter array becomes the nums1 to minimise the search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        full = m + n
        half = (full + 1) // 2 # the number of elements in the left partition

        left = 0
        right = m

        while left <= right:

            cut1 = (left + right) // 2
            cut2 = half - cut1

            # use infinities for empty partition boundaries
            left_max_num1 = nums1[cut1 - 1] if cut1 > 0 else float ('-inf') # negative infinity
            left_max_num2 = nums2[cut2 - 1] if cut2 > 0 else float ('-inf')
            right_min_num1 = nums1[cut1] if cut1 < m else float ('inf') # positive infinity
            right_min_num2 = nums2[cut2] if cut2 < n else float ('inf')

            if left_max_num1 <= right_min_num2 and left_max_num2 <= right_min_num1:
                if full % 2 == 1:
                    return max(left_max_num1, left_max_num2)
                else:
                    return (max(left_max_num1, left_max_num2) + min(right_min_num1, right_min_num2)) / 2

            elif left_max_num1 > right_min_num2: # less elements required in the left partition from nums1
                right = cut1 - 1

            elif left_max_num2 > right_min_num1: # more elements required in the left partition from nums1
                left = cut1 + 1