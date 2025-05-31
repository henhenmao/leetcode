
from typing import List

"""
74. Search a 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/)
You must write a solution in O(log(m * n)) time complexity.

you pretty much gotta do a double binary search
    you can do this since you know all rows in matrix are sorted and numbers within rows are sorted
first binary search to find the correct row interval
then binary search within the row to find the number

algorithm:
    1. perform a binary search to find the correct row 
        compare the target to the first elements of each row
    2. perform binary search inside of the row once you've found it
    
runtime: O(log(n) + log(m)) = O(log(n * m))
space: O(1)
"""


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    i = -1 # will be set to the row we want to search within

    # finding the correct row number to search for 
    low = 0
    high = len(matrix)-1

    while low <= high:
        mid = (low + high) // 2
        if target >= matrix[mid][0] and target <= matrix[mid][-1]: # if target is inside current mid row
            i = mid
            break
        if matrix[mid][0] <= target: # target is above or equal to the mid pointer's row
            low = mid+1
        elif matrix[mid][0] > target: # target is strictly below the mid pointer's row
            high = mid-1

    row = matrix[i] 
    if not (target >= row[0] and target <= row[len(row)-1]):
        return False
    
    low = 0
    high = len(row)-1

    while low <= high:
        mid = (low+high)//2

        if row[mid] == target:
            return True

        elif row[mid] < target:
            low = mid+1

        elif row[mid] > target:
            high = mid-1
    return False


"""
below solution is NOT valid
i thought it was valid when i submitted it a few months ago
i traversed through matrix linearly and only binary searched within the rows
runtime: O(n * log(m))
still somehow faster than 100% of people on leetcode
    its inaccurate most of the time anyways

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
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



"""

