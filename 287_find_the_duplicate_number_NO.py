

from typing import List

"""
287. Find the Duplicate Number (https://leetcode.com/problems/find-the-duplicate-number/description/)
You must solve the problem without modifying the array nums and using only constant extra space.
Follow up:
    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?

ok i "accidentally" was spoiled the solution and now i know that i should be using floyds tortoise and hare algorithm to detect cycles
    if each index points to a value at the index (i -> nums[i])
    since there is a duplicate in nums, there must be a cycle
    pretty much kind of like what i did before but with a pointer method instead of modifying the list directly

    

"""
def findDuplicate(nums: List[int]) -> int:
    pass



"""
i didn't read the problem well enough and solved the question by modifying the array:
    use nums as the hash set
    we don't care about the non duplicate value indexes
    because they don't matter to us
    for each value of nums[i]:
    hash nums[nums[i]-1] as a value like -1
    if nums[nums[i]-1] is already -1 then you found the duplicate

    ok since nums[i] is always positve we can just mark numbers as negative and use absolute values

"""
def findDuplicate(nums: List[int]) -> int:
    for i in range(len(nums)):
        curr = abs(nums[i])
        if nums[curr] < 0:
            return(abs(nums[i]))
        else:
            nums[curr] *= -1

nums = [1,2,3,4,4]
print(findDuplicate(nums))

