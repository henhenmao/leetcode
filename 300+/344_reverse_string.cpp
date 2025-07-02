
/*
344. Reverse String (https://leetcode.com/problems/reverse-string/description/)
You must do this by modifying the input array in-place with O(1) extra memory.

simple code loops a pointer through the first half of the string list
each index i will be swapped with the index on the other side of the string list
    index i is swapped with index s.size()-1-i

ex. s = ['a', 'b', 'c', 'd', 'e']
    index 0 is swapped with index 4
    index 1 is swapped with index 3
    end of loop
    s = ['e', 'd', 'c', 'b', 'a']

algorithm:
    1. loop through just first half of the list
    2. for each index i, swap the element at index i with the element at index s.size()-1-i

runtime: O(n) where n is the length of s
space: O(1)
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void reverseString(vector<char>& s) {
    int j;
    for (int i = 0; i < s.size()/2; i++) {
        j = s.size()-1-i; 
        swap(s[i], s[j]);
    }
}