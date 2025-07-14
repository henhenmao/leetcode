

"""
41. First Missing Positive (https://leetcode.com/problems/first-missing-positive/description/)
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


what if i had O(n) space available:
    i would just use a hash set and starting at n = 0, check if n+1 exists until it doesn't

given an integer n, how to prove that n+1 exists or not in the array without extra memory?

things:
    - if the minimum value in nums is greater than 1, the solution is 1
    - if all values from 1 to n, solution is max(nums)+1

dude i actually have no idea
ts is cooked
"""



