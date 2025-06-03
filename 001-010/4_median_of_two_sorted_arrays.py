
from typing import List

"""
4. Median of Two Sorted Arrays (https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
The overall run time complexity should be O(log (m+n))

i did NOT solve this in the intended way but i'm just going to put this here
what's really funny is that when i first started out i thought i was so smart for doing this in a few lines

i bet the real solution is crazy difficult





this question probably took at least a month off of my lifespan

note the following things:
    n = len(nums1), m = len(nums2)
    assume nums1 is less than nums2

    - you know the total length of the merged sorted list = n + m
        - therefore the median of the merged sorted list is somewhere around the (n+m)//2 area
    - if you look at the first i elements of nums1, you know you should look at the first ((n+m)//2 - i) elements of nums2
    - we can then compare the last element (max element) of each of these partitions and check for validity
- we are essentially searching for the correct partition of nums1, which leads to the correct partition in nums2


algorithm:
    1. out of nums1 and nums2 determine which one has a smaller size
        you want to begin the partitioning on the lesser of the two
        label nums1 to be the smaller list and nums2 to be the larger
    2. prepare a binary search on nums1 by setting two pointers on each end
    3. when binary searching nums1, each mid = (low + high)//2 value represents the partition of the first (mid) elements you want to use in nums1
    4. if using first (mid) elements of nums1, you know you must use the first ((n+m)//2 - (mid) - 2) of nums2
        the -2 is there because of zero index on both nums1 and num2

    5. keep track of the max value (rightmost) of the left partition and the min value (leftmost) of the right partition for both arrays
        max value of left partition for nums1 and nums2 = left1 and left2
        min value of right partition for nums1 and nums2 = right1 and right2

    6. test if the partition is valid by seeing if (left1 is less than right2) and (left2 is less than right1)

        if both conditions pass: you know you have perfectly partitioned the two arrays for the first ((n+m)//2) values of the merged sorted array
            all that is left is return the median based
            if total length is odd, the median is either right1 or right2, return the minimum of the two
            if total length is even, the median is the mean of max(left1, left2) and min(right1, right2)

        if one of the conditions don't pass: you know that nums1 could be partitioned better
            if left2 > left1, you undershot the partition and must continue the binary search to go up
            if left1 > left2, you overshot the partition and must continue the binary search to go down

runtime: O(log(n+m)) where n and m are the lengths of nums1 and nums2
space: O(1)
"""



def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    n = len(nums1)
    m = len(nums2)

    total = n + m
    half = total//2

    low = 0
    high = n-1

    while True:
        a = (low + high)//2
        b = half-a-2 # subract by two because both lists are zero indexed

        left1 = nums1[a] if a >= 0 else float("-infinity")
        right1 = nums1[a+1] if (a+1) < n else float("infinity")

        left2 = nums2[b] if b >= 0 else float("-infinity")
        right2 = nums2[b+1] if (b+1) < m else float("infinity")

        # if the partition is correct
        if left1 <= right2 and left2 <= right1:
            # get mean of the medians if even length
            if total % 2 == 1: # odd number
                return min(right1, right2)
            return (max(left1, left2)+min(right1, right2))/2

        # if the partition is off
        elif left2 > left1: # left1 is too small -> extend left1
            low = a+1
        elif left1 > left2:
            high = a-1

"""
funny inefficient solution

runtime: O((n+m) * log(n+m)) where n and m are the lengths of nums1 and nums2
space: O(n+m)
"""

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1 + nums2)
        if len(new_list) % 2 == 1:
            return new_list[len(new_list)//2]
        return (new_list[len(new_list)//2] + new_list[len(new_list)//2-1])/2