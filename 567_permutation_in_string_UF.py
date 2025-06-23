

"""
567. Permutation in String (https://leetcode.com/problems/permutation-in-string/description/)

can't use a set since there can be duplicate values in s1
convert s1 into a frequency table of all letters

freq = {"a":1, "b":1}

use a sliding window for s2 to count down the frequencies on the s1 hash table
    use two pointers i and j to denote the start and end of the current substring to check in s2
        put pointers i and j so that s[i:j+1] is size k -> k == (j-i+1)
    if s2[j] in freq and freq[s2[j]] is greater than 1:
        count down freq[s2[j]]
    if not in freq or frequency is 0, move the window up by one

moving window up:
    before moving i up, add one back to freq[s2[i]] since we aren't looking at it anymore
    move j up and look at the new character at s2[j]

when do have the solution:
    at the start set a total counter set at len(s1)
        every time a character is decremented in the hash map, decrement the total counter
        every time a character is incremented in the hash map, increment the total counter

runtime: O(n+m) where n is len(s1) and m is len(s2)
space: O(n) where n is the length of s1

"""

def checkInclusion(s1: str, s2: str) -> bool:

    if len(s2) < len(s1):
        return False

    total = len(s1) # if total == 0 return true
    freq = {}
    for c in s1:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    i = 0
    j = 0 # just increment j at the start and increment i when (j-i+1) == len(s1)
    
    # add the initial values covered by s[i:j] 

    print(freq)

    while j < len(s2):
        if (j-i+1) < len(s1): # icrement just j
            if s2[j] not in freq or freq[s2[j]] == 0:
                i += 1
                j += 1

                
            else:
                freq[s2[j]] -= 1
                total -= 1
                j += 1
        else: # incrementing both i and j
            if s2[j] not in freq or freq[s2[j]] == 0:
                i += 1
                j += 1
                # remove the ith index
                freq[s2[i]] += 1
                total += 1
            else:
                freq[s2[j]] -= 1
                total -= 1
        
        if total == 0:
            return True
    return False


s1 = "ab"
s2 = "eidboaooo"
print(checkInclusion(s1, s2))