

/*
869. Reordered Power of 2 (https://leetcode.com/problems/reordered-power-of-2/?envType=daily-question&envId=2025-08-10)

given two integers, we can compare whether or not the numbers can be rearranged if they contain the same digit frequencies
    idk about the leading zero cannot be zero and if that's an edge case or not

i'm just going to just count every power of two from 1 to 10^9 and compare the digit freqeuncies
    should be O(log(n))


*/

#include <iostream>
#include <unordered_map>
using namespace std;

bool reorderedPowerOf2(int n) {

    unordered_map<int, int> freq;
    for (char c : to_string(n)) {
        freq[c]++;
    }

    int i = 1;

    while (i < (pow(10, 9))) {
        unordered_map<int, int> freq2;
        for (char c : to_string(i)) {
            freq2[c]++;
        }

        if (freq == freq2) {
            return true;
        }

        i *= 2;
    }
    return false;
}

int main() {
    int n = 3;
    cout << reorderedPowerOf2(n);
    return 0;
}