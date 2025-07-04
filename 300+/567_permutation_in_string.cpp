


/*
567. Permutation In String (https://leetcode.com/problems/permutation-in-string/)

1. convert s1 into a frequency table of all letters
2. maintain a sliding window of size s1 over s2
3. keep track of the letter frequencies of the current sliding window
4. if the letter frequencies of the window match the frequencies of s1, return true

algorithm:
    1. first check that length of s1 is less than or equal to length of s2
        if this is not true then s2 cannot contain s1 as a permutation so return false
    2. create letter frequency hashmaps for both s1 and s2
    3. get letter frequency for all letters of s1
    4. build letter frequency for the first s1.length() letters in s2, this is the current sliding window
    5. set pointers for the sliding window at i=0 and j=s1.length()
    6. move the sliding window by adding frequency of s2[j] and decrementing frequency of s2[i] when the window moves
    7. if the sliding window frequency ever is the same as the s1 frequency, that is your permutation and return true

runtime: O(n+m) where n is length of s1 and m is the length of s2
space: O(1) since the hash maps will always hold at most 26 letter keys
*/

#include <iostream>
#include <unordered_map>
using namespace std;

bool checkInclusion(string s1, string s2) {
    int n1 = s1.length();
    int n2 = s2.length();

    if (n1 > n2) {
        return false;
    }

    // get the frequencies of each letter in s1
    unordered_map<char, int> freq1;
    unordered_map<char, int> freq2;

    for (int i = 0; i < n1; i++) {
        freq1[s1[i]]++;
        freq2[s2[i]]++;
    }

    if (freq1 == freq2) {
        return true;
    }

    int i = 0;
    for (int j = n1; j < n2; j++) {
        freq2[s2[j]]++;
        freq2[s2[i]]--;

        if (freq2[s2[i]] == 0) {
            freq2.erase(s2[i]);
        }

        i++;
        
        if (freq1 == freq2) {
            return true;
        }
    }
    return false;    
}

int main() {

    string s1 = "dinitrophenylhydrazine";
    string s2 = "dimethylhydrazine";

    cout << checkInclusion(s1, s2) << endl;
    return 0;

}