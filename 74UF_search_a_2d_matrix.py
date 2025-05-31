
from typing import List

"""
74. Search a 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/)
You must write a solution in O(log(m * n)) time complexity.

you pretty much gotta do a double binary search
    you can do this since you know all rows in matrix are sorted and numbers within rows are sorted
first binary search to find the correct row interval
then binary search within the row to find the number

"""


# write correct solution here



"""
below solution is NOT valid
i thought it was valid when i submitted it a few months ago
i traversed through matrix linearly and only binary searched within the rows
runtime: O(n * log(m))
still somehow faster than 100% of people on leetcode
    its inaccurate most of the time anyways
"""

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    for nums in matrix:
        if target >= nums[0] and target <= nums[len(nums)-1]:
            low = 0
            high = len(nums)-1

            while low <= high:
                mid = (low+high)//2


                if nums[mid] == target:
                    return True

                elif nums[mid] < target:
                    low = mid+1

                elif nums[mid] > target:
                    high = mid-1
            return False
    return False