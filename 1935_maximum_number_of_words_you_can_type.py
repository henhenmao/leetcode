

"""
1935. Maximum Number of Words You Can Type (https://leetcode.com/problems/maximum-number-of-words-you-can-type/?envType=daily-question&envId=2025-09-14)

for each word in the text string, check if any broken letters appear
    if a single broken letter appears in the current word, do not count it in the count

algorithm:  
    1. split each word by spaces into a list of separate words
    2. for each word, add 1 to the count
    3. iterate through each character in the word
        if a broken character in found in the word, decrement 1 from the count

runtime: O(n * k) where n is the length of text and k is the length of brokenLetters
space: O(n)
"""


def canBeTypedWords(text: str, brokenLetters: str) -> int:

    count = 0
    words = text.split(" ")

    for word in words:
        for c in brokenLetters:
            if c in word:
                count -= 1
                break
        count += 1

    return count

text = "leet code"
brokenLetters = "lt"
print(canBeTypedWords(text, brokenLetters))