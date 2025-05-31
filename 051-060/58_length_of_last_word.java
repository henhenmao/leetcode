

/* 
58. Length of Last Word (https://leetcode.com/problems/length-of-last-word/description/)

in python you can just do return len(s.split()[-1])
literally no difference in java

algorithm:
    1. split the string by spaces and create a new list containing words
    2. take the last element in that list and return the length

runtime: O(n), where n is the length of s
space: O(n)
*/

class Solution {
    public int lengthOfLastWord(String s) {
        String[] res = s.split(" ");
        return res[res.length-1].length();
    }
}

