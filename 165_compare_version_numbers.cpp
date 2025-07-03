

/*
165. Compare Version Numbers (https://leetcode.com/problems/compare-version-numbers/description/)

use pointers to iterate through version1 and version2, using the "."s as breakpoints
one at a time, use a pointer to follow revisions for version1 until a "." is encountered
do the same thing for version2

compare the two revision values.
if both are equal, repeat previous steps
if one is greater, return -1 or 1 as stated in problem

if pointer reaches the end of string and no more revisions for a version, just skip the pointer stuff and set revision to 0

runtime: O(n) where n is the length of version1 and version2
space: O(n)

*/

#include <iostream>
using namespace std;


int compareVersion(string version1, string version2) {
    int p1 = 0;
    int p2 = 0;

    int n1 = version1.length();
    int n2 = version2.length();

    // while at least one pointer is still in bounds
    while (p1 < n1 || p2 < n2) {

        // check individual revisions
        string v1 = "";
        string v2 = "";

        if (p1 < n1) {
            while (p1 < n1 && version1[p1] != '.') {
                v1 += version1[p1];
                p1++;
            }
            p1++;
        } else {
            v1 = "0";
        }

        if (p2 < n2) {
            while (p2 < n2 && version2[p2] != '.') {
                v2 += version2[p2];
                p2++;
            }
            p2++;
        } else {
            v2 = "0";
        }

        int revision1 = stoi(v1);
        int revision2 = stoi(v2);

        if (revision1 > revision2) {
            return 1;
        } else if (revision1 < revision2) {
            return -1;
        }
    }
    return 0;

}

int main() {
    string version1 = "1.0";
    string version2 = "1.0.0.0.0";

    cout << compareVersion(version1, version2) << endl;
    return 0;
}
