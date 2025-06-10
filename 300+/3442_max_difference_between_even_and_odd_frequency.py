



"""
3442. Maximum Difference Between Even and Odd Frequency I (https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10)

algorithm:
    1. count the frequencies of each character in the string using a hashmap
    2. find the maximum odd frequency 
    3. find the minimum even frequency
    4. return the difference between the above two values

runtime: O(n) where n is the number of characters in the string
space: O(n)
"""

def maxDifference(s: str) -> int:
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else: 
            freq[c] = 1

    max_odd = -200
    min_even = 200
    for k, v in freq.items():
        if v % 2 == 0: #even
            min_even = min(v, min_even)
        else:
            max_odd = max(v, max_odd)
    
    return max_odd - min_even