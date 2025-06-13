
"""
981. Time Based Key-Value Store (https://leetcode.com/problems/time-based-key-value-store/description/)

we are only dealing with three values: key, value, and timestamp
when the get(key, timestamp) function is called, we search for all values in the timemap with the same key and a matching timestamp

to make our life easy, we can use a hashmap to store each key with it's corresponding value and timestamp
    when we use the get(key, timestamp) call, we can easily access a list of all timestamps with the matching key in O(1) time
        with access to the list of timestamps, we can just binary search for the most recent time that is less than or equal to the input timestamp

init:
    create hashmap timemap to store {key: [value, timestamp]}

set:
    if given key does not exist in timemap, create a new key in timemap and add value and timestamp
    if given key already exists in the timemap, add value and timestamp to the list

get:
    find the list of values with matching key
    perform a binary search within all timestamps with the matching key
    keep track of the most recent time that is less than or equal to the input time


runtime:
    set(): O(1)
    get(): O(log(n)) where n is the size of the hashmap

space: O(n) 
"""

class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # check if the key exists in the hashmap already
        if key in self.timemap:
            self.timemap[key].append([value, timestamp])
        else:
            self.timemap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap: # no need to search if key doesn't exist at all
            return ""
        
        # perform a binary search for most recent time under timpstamp in self.timemap[key]
        low = 0
        high = len(self.timemap[key])-1
        res = -1 # to get the most recent time

        # self.timemap[key][mid] = [value, timestamp]
        while low <= high:
            mid = (low + high)//2

            if self.timemap[key][mid][1] <= timestamp:
                res = self.timemap[key][mid][0]
                low = mid+1
            else:
                high = mid-1
        
        if res == -1:
            return ""
        return res