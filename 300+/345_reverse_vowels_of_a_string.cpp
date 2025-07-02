

/*
345. Reverse Vowels of a String (https://leetcode.com/problems/reverse-vowels-of-a-string/description/)

will just use a two pointer technique to find pairs of vowels closing in on both ends

algorithm:
    1. set left pointer at 0 and right pointer at s.length()-1
    2. move the left pointer to the right and stop at the first vowel encountered
    3. move the right pointer to the left and stop at the first vowel encountered
    4. swap the vowels at left pointer and right pointer
    5. repeat steps 2-4 until left and right pointers meet at the same vowel (odd vowels) or pass each other (even vowels)

runtime: O(n)
space: O(1)
*/

#include <iostream>
using namespace std;

bool isVowel(char c) {
    string vowels = "aeiouAEIOU";
    return (vowels.find(c) != string::npos);
}

string reverseVowels(string s) {
    int left = 0;
    int right = s.length()-1;

    while (left < right) {
        // move left pointer until vowel
        while (left < right && !isVowel(s[left])) {
            left += 1;
        }

        // move right pointer until vowel
        while (left < right && !isVowel(s[right])) {
            right -= 1;
        }
        
        // swap left and right indexes
        swap(s[left], s[right]);
        left += 1;
        right -= 1;
    }
    return s;
}

int main() {
    string s = ".,";
    cout << reverseVowels(s) << endl;
    return 0;
}