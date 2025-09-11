

"""
295. Find Median from Data Stream (https://leetcode.com/problems/find-median-from-data-stream/description/?envType=problem-list-v2&envId=oizxjoit)

just keep a sorted array of all numbers added so far
use a binary search to find the median of the current sorted array whenever the findMedian function is called

addNum
    


"""


class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass
    
    def findMedian(self) -> float:
        pass


medianfinder = MedianFinder()
medianfinder.addNum(1)
medianfinder.addNum(2)
medianfinder.findMedian() # returns 1.5
medianfinder.addNum(3)
medianfinder.findMedian() # returns 2.0