
from typing import List
from collections import deque

"""
1298. Maximum Candy You Can Get From Boxes (https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/?envType=daily-question&envId=2025-06-03)

n boxes (0 to n-1)
four arrays: status, candies, keys, containedBoxes
    - status[i] = 1 is open and 0 if closed
    - candies[i] = number of candies in the ith box
    - keys[i] = the list of boxes you can open after opening ith box
    - containedBoxes[i] = list of boxes you found in the ith box

can probably use bfs to search every available box
    unlock each possible key you can get your hands on and add it to the queue
    have a visited array so you don't go in circles
    i honestly have no idea what else there is to do

for each box:
    - check if visited
    - take candies
    - add boxes to queue only if you have their keys
    - mark box as visited

i forgot to read the last part of the question where it gives me initialBoxes
    maybe i should read the full question before doing it


algorithm:
    1. create a queue for bfs and a hash set to contain all your keys
    2. go through the initialBoxes and add all open boxes and take all keys from open boxes
    3. if a box is opened, add only the boxes that you can open in the queue
        these are the boxes that are either already opened (status[i] == 1)
        or boxes that are locked but have the key (status[i] == 0 and i in haveKeys)
    4. basically for the rest of the bfs we repeat these steps:
        a. pop the box from the top of the stack (curr)
        b. for all boxes in curr, do a loop to see if you can scrap out any new keys from what you have
        c. after getting all the keys you can, do another loop to see which boxes you can open
        d. add boxes that you can open into the queue
        we make sure that we strictly can only open boxes that are either already unlocked or can be unlocked with a key we have

runtime: O(n) where n is the number of boxes i think (not sure)
space: O(n)
"""

def maxCandies(status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
    # create queue and visited array
    n = len(candies)
    queue = deque([]) # contains all pushed keys
    candyCount = 0
    haveKeys = set()

    # initial pass: getting all available keys
    # second pass: open all boxes available if keys for box exists
    for box in initialBoxes:
        if status[box] == 1 or (status[box] == 0 and box in haveKeys):
            for key in keys[box]:
                haveKeys.add(key)

    for box in initialBoxes:
        # can only open a box if the box is already unlocked or have the key
        # if status[box] == 2 or (status[box] == 0 and box not in haveKeys):
        #     continue
        if status[box] == 1 or (status[box] == 0 and box in haveKeys):
            candyCount += candies[box]
            queue.append(box)
            status[box] = 2

    while queue:
        curr = queue.popleft() # curr is a key 

        for box in containedBoxes[curr]:
            if status[box] == 1 or (status[box] == 0 and box in haveKeys):
                for key in keys[box]:
                    haveKeys.add(key)
                
        for box in containedBoxes[curr]:
            if status[box] == 1 or (status[box] == 0 and box in haveKeys):
                candyCount += candies[box]
                queue.append(box)
                status[box] = 2
        
    return candyCount


# status = [1,0,1,0]
# candies = [7, 5, 4, 100]
# keys = [[], [], [1], [3]]
# containedBoxes = [[1, 2], [3], [], []]
# initialBoxes = [0]

# print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))