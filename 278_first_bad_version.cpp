

/*
278. First Bad Version (http://leetcode.com/problems/first-bad-version/description/)

this looks like a binary search question 
binary search for the first version that returns true for isBadVersion()

algorithm:
    1. set low and high pointers at the beginning and end of the versions
    2. if isBadVersion(mid) is false, we know the bad version appears later on the in the list
        set low to mid and check the right side
    3. if isBadVersion(mid) is true, we know the bad version is either at mid or appeared somewhere before
        set high to mid and check the left side
    4. eventually when the binary search ends, high will point to the first bad version

runtime: O(log(n))
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

vector<bool> versions = {true};

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);
bool isBadVersion(int version) {
    // stuff happens here
    return 0;
}

long firstBadVersion(long n) {
    long low = 1;
    long high = n;
    long mid;

    while (low < high) {
        mid = (low+high)/2;

        if (isBadVersion(mid)) {
            high = mid;
        } else {
            low = mid+1;
        }
    }
    return high;
}