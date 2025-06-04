


from heapq import _heapify_max, _heappop_max, _siftdown_max


"""
3403. Find the Lexograhpically Largest String From the Box I (https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/?envType=daily-question&envId=2025-06-04)

let n be the length of word
and k be the number of friends
is the answer always length n-k+1
    meaning we just get substrings of length (n-k+1)

may need to sort the string to be in some lexigraphic order
    nevermind you can't sort the string since we are partitioning not getting subsets
could use  max heap and return the top maybe

get all substrings of length (n-k+1) using a sliding window
    compare each string and keep track of the maximum
probably O(n^2) time so pretty slow unfortunately

algorithm:
    1. we calculate the ideal length of the solution as (n-k) where n = len(word) and k = numFriends
        pretty much assuming that the partition involves the other k-1 friends only getting one character in the split
    2. use a sliding window to traverse all substrings of length (n-k) in word
        keep updating the maximum string you have encountered (lexographically largest)
    3. we want the right pointer to go past word[n] since a possible solution could be less than length (n-k) but only if it cut off at the end of word
    4. there's a single edge case involving k = 1 since n partitions can be made in the first place, in that case just return the word directly

runtime: O(n^2) where n is the length of word
space: O(n)  
"""


def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
            return word

    n = len(word)

    i = 0
    sz = n-numFriends+1 # size of the solution probably

    res = ""

    while i < n:
        if sz > n:
            sz = n

        temp = word[i:sz]
        i += 1
        sz += 1
        res = max(res, temp)
    return res



    

    