


/*
3227. Vowel Games in a String (https://leetcode.com/problems/vowels-game-in-a-string/description/?envType=daily-question&envId=2025-09-12)

the winner of the vowel game is probably just dependent of the parity of the number of vowels in the starting string
    taking into account that Alice, who takes an odd number of vowels, always goes first

let k be the number of vowels in the string

if there are no starting vowels
    alice loses

if there are an odd number of starting vowels:
    alice can take away the entire string that contains k vowels and bob is left with an empty string 

if there are an even number of starting vowels:
    alice can take away k-1 vowels, leaving only one vowel left
    since there is one vowel left, there is no way for bob to win the game, and alice can simply take away the entire string on her next turn

i'm a little confused on how alice can lose the game aside from the case where starting vowels == 0

algorithm:
    1. count the number of vowels in the string
    2. if there are zero vowels in the string, return false
    3. otherwise, return true

runtime: O(n) where n is the size of the string
space: O(1)
*/

#include <iostream>
using namespace std;

bool doesAliceWin(string s) {
    string vowels = "aeiouAEIOU";
    int vowelsCount = 0;

    for (char c : s) {
        if (vowels.find(c) != std::string::npos) vowelsCount++;
    }

    if (vowelsCount == 0) {
        return false;
    }
    return true;
}

int main() {
    string s = "hello";

    doesAliceWin(s);

    return 0;
}