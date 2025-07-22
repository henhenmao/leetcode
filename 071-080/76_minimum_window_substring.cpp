

/*
76. Minimum Window Substring (https://leetcode.com/problems/minimum-window-substring/description/)
Follow up: Could you find an algorithm that runs in O(m + n) time?

string s of length m
string t of length n
return minimum window substring of s that contains every character in t (duplicates included)


the next 12 lines did not work
(i was in the right direction but i made silly mistakes)
    i'm pretty sure we should keep track of the character frequencies in t
    do a sliding window of some sort
        i do not know what condition is needed to shift the left pointer of the window yet
        i need to think about this

    ok so we should just shift the left pointer the moment we have a valid substring of s that contains all characters in t
        if you just keep expanding the window from index 0 to index i, s[0:i] will eventually contain a valid substring
            (assuming that an answer exists)

        once we find a valid substring, we just need to find the latest index where the valid substring can begin
            by shifting the left pointer of the window until the window does not contain a valid substring anymore


algorithm that actually worked:
    1. count the frequecy of characters in t into hashmap tfreq

    2. initialize another hashmap currFreq, int currUnique, and int totalUnique
        currFreq[c] gives the frequency of character c in the current window
        totalUnique is the number of distinct characters in t
        currUnique is the number of characters c in which currFreq[c] >= tfreq[c]
            essentially just how many characters in the current window have met the requirement

    3. set pointers left and right at the start of s

    4. expand the window by shifting right pointer
        add every element of s[right] into currFreq (currFreq[s[right]]++)
            if a character meets it's requirements (currFreq[s[right]] >= tfreq[s[right]]), increment currUnique by 1
        repeat previous three lines until currUnique == totalUnique
        currUnique == totalUnique means that every distinct character has fullfilled the requirement
    
    5. when currUnique == totalUnique, you have a valid substring at s[left:right]
        compare the length of the substring (right-left+1) to the current minimum length so far and update if needed
    
    6. when you have a valid substring, shift the left pointer until s[left:right] is not a valid substring anymore


runtime: O(n + m) where m is the length of s and n is the length of t
space: O(n) where n is the length of t
*/


#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

string minWindow(string s, string t) {
    
    // building frequency of characters in t
    unordered_map<char, int> tfreq;
    for (char c: t) {
        tfreq[c]++;
    }

    // keep track of unique characters seen

    unordered_map<char, int> currFreq;
    int currUnique = 0, totalUnique = tfreq.size();

    string minString;
    int left = 0, right = 0;

    // res_i will contain the start index of the result minimum substring
    int res_i = 0;
    int minLength = INT_MAX;

    while (right < s.length()) {

        char curr = s[right];
        currFreq[curr]++;

        if (tfreq.count(curr) && currFreq[curr] == tfreq[curr]) {
            currUnique++;
        }

        // shift the left pointer while the window contains all characters from t
        while (currUnique == totalUnique) {

            // since window contains valid substring, check the length of window
            // compare to the minimum so far
            if (right-left+1 < minLength) {
                res_i = left;
                minLength = right-left+1;
            }

            // cout << "current substring: " << s.substr(left, right-left+1) << endl << "minLength = " << minLength << endl << "n = " << n << endl << endl;

            
            char currLeft = s[left];
            currFreq[currLeft]--;


            if (tfreq.count(currLeft) && currFreq[currLeft] < tfreq[currLeft]) {
                currUnique--;
            }
            left++;
        }

        right++;
    }
    return minLength != INT_MAX ? s.substr(res_i, minLength) : "";
}

int main() {

    string s = "bbaac";
    string t = "aba";

    cout << minWindow(s, t) << endl;

    return 0;
}