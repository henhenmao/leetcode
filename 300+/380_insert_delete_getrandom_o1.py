

import random


"""
380. Insert Delete GetRandom O(1) https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
You must implement the functions of the class such that each function works in average O(1) time complexity.

we need to be able to check whether or not a value exists in the set in O(1) time
we also need to be able to remove any value from the set in O(1) time
these two functions are already implemented in the set data structure

we finally need to be able to get a random element from the set, where each value has the exact same probability of being selected
    this means that we cannot use a set
    must use a data structure with indexing like a list
        so you can call a random number between indexes 0 and set.size()-1 and return list[i]

we can use a combo of a hash map and array to implement set functions
let dict = hash map
    arr = array

insert(val)
    check if val exists already as a key in dict
    append val to the end of arr, arr[i] = val
    hash key value pair of val: i in dict

remove(val)
    check if val exists already as a key in dict
    let i = dict[val]
    since we are implementing a set, the order of arr doesn't matter 
    we can simply swap the values of arr[i] and arr[-1], and then pop from the end of arr
        also make sure to swap the values in dict
        
    finally we can remove the key value pair of i and val in dict

    arr[i] = val
    arr[i] = arr[-1]
    arr.pop()
    dict.pop(val)

getRandom()
    use random function for random arr index in the range (0, len(nums)-1)

    
runtime: O(1) for each function
space: O(n) where n is the max number of elements dict and arr hold at a time
"""

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        # swapping values of arr[i] and arr[-1] and then popping
        i = self.dict[val]
        self.dict[self.arr[-1]] = i # setting dict value of the last element to i since its getting relocated
        self.arr[i] = self.arr[-1]
        self.arr.pop()
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.arr)-1)
        return self.arr[i]

