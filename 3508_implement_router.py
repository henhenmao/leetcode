

from collections import deque
from typing import List
import bisect

"""
3508. Implement Router (https://leetcode.com/problems/implement-router/?envType=daily-question&envId=2025-09-17)

source: A unique identifier for the machine that generated the packet
destination: A unique identifier for the target machine
timestamp: The time at which the packet arrived at the router

use a deque to simulate the FIFO of the packets
add all packets into a sets to detect duplicates 
use a hashmap for counting in getCount
    use a key value pair of destination : timestamp
have an integer that always keeps track of the number of packets that the router holds

Router():
    initialize the deque
    initialize the hashmap
    initialize the set
    set packetCount to 0
    also store the memory limit somewhere

addPacket():
    check if destination exists in the hashmap as a key AND that hashmap[destination] == [source, timestamp]
        if this is true, there is an exact duplicate and you should return False

    also check if packetCount will exceed the memory limit
        if true: remove the front packet from all data structures
            decrement packetCount
            remove from duplicate set
            pop the leftmost element from list of destinations (that is the oldest packet)

    add the [source, destination, timestamp] to the end of the queue
    add the packet info to the set as a tuple
    append the timestamp to the proper destination list
    add 1 to the packetCount
    return True

forwardPacket():
    if the queue is empty, return empty array     

    decrement packetCount
    dequeue the packet at the front of the queue
    remove the source of that packet from the set
    return the packet info

getCount():
    get the list of packets that match the proper destination from the packets hashmap
        this list should be sorted by timestamp
    use python bisect on the list to get the range of timestamps that fulfill the criteria

runtime:
    Router(): O(1)
    addPacket(): O(1)
    forwardPacket(): O(1)
    getCount(): O(log(n))

space: O(n) where n is the memory limit of the router
"""

class Router:

    def __init__(self, memoryLimit: int):
        self.queue = deque([])
        self.packets = {}
        self.duplicates = set()
        self.packetCount = 0
        self.memoryLimit = memoryLimit
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.duplicates:
            return False
        
        # if memory exceeded, remove the oldest packet from everything
        if self.packetCount == self.memoryLimit:
            self.packetCount -= 1
            oldSource, oldDestination, oldTimestamp = self.queue.popleft()
            self.duplicates.remove((oldSource, oldDestination, oldTimestamp))
            self.packets[oldDestination].popleft() # oldest packet in the matching destinations

        # adding to queue, set, and hashmap
        self.queue.append([source, destination, timestamp])
        self.duplicates.add((source, destination, timestamp))

        if destination in self.packets:
            self.packets[destination].append(timestamp)
        else:
            self.packets[destination] = deque([timestamp])

        self.packetCount += 1
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []

        source, destination, timestamp = self.queue.popleft()
        packet = [source, destination, timestamp]
        self.duplicates.remove((source, destination, timestamp))
        self.packets[destination].popleft()
        self.packetCount -= 1
        return packet
        
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.packets:
            return 0
        
        left = bisect.bisect_left(self.packets[destination], startTime)
        right = bisect.bisect_right(self.packets[destination], endTime)
        return right-left
        

# router = Router(3)
# router.addPacket(1, 4, 90)
# router.addPacket(2, 5, 90)
# router.addPacket(1, 4, 90)
# router.addPacket(3, 5, 95)

# router.addPacket(4, 5, 105)
# print(router.queue)
# print(router.duplicates)
# print(router.packets)
# print()

# print(router.forwardPacket())

# router.addPacket(5, 2, 110)
# print(router.queue)
# print(router.duplicates)
# print(router.packets)
