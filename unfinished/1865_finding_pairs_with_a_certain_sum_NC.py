

from typing import List

"""
1865. Finding Pairs With a Certain Sum (https://leetcode.com/problems/finding-pairs-with-a-certain-sum/?envType=daily-question&envId=2025-07-06)


too tired to write comments 
i need a hug

"""

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.freq1 = {}
        self.freq2 = {}

        self.nums1 = nums1
        self.nums2 = nums2

        for n in self.nums1:
            if n in self.freq1:
                self.freq1[n] += 1
            else:
                self.freq1[n] = 1
        
        for n in self.nums2:
            if n in self.freq2:
                self.freq2[n] += 1
            else:
                self.freq2[n] = 1
        
    def add(self, index: int, val: int) -> None:
        prev_val = self.nums2[index]
        new_val = prev_val + val

        # updating the frequency map
        self.freq2[prev_val] -= 1
        if self.freq2[prev_val] == 0:
            del self.freq2[prev_val]

        if new_val in self.freq2:
            self.freq2[new_val] += 1
        else:
            self.freq2[new_val] = 1

        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        count = 0
        for k1, v1 in self.freq1.items():
            if tot-k1 in self.freq2:
                count += self.freq2[tot-k1] * v1
        return count

nums1 = [1,1,2,2,2,3]
nums2 = [1,4,5,2,5,4]
a = FindSumPairs(nums1, nums2)
print(a.count(7))