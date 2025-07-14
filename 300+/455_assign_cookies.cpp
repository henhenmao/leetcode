

/*
455. Assign Cookies (https://leetcode.com/problems/assign-cookies/description/)
Note: This question is the same as 2410: Maximum Matching of Players With Trainers.

sort the greed array and the cookie size array in non decreasing order
put pointer at the beginning of each array, let i be the pointer at array g and j be the pointer at array s
see if the greed of the ith kid g[i] can be satisfied with the size of the jth cookie s[j]
if can be satisfied, increment both i and j and add 1 to the total
if cannot be satisfied, increment just j as we now know that the jth cookie will not be able to sate any more kids

runtime: O(n * log(n) + n * log(m)) where n is the length of g and m is the length of s, sorted both arrays
space: O(1)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0;
    int j = 0;
    int cookies = 0;

    while (i < g.size() && j < s.size()) {
        if (s[j] >= g[i])  {// current cookie will satisfy the current child
            cookies++;
            i++;
        }
        j++;
    }
    
    return cookies;
}


int main() {
    return 0;
}