

/*
3304. Find the K-th Character in String Game I (https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/description/?envType=daily-question&envId=2025-07-03)

lowercase alphabet ascii values - 97-122

recursive function to find kth character:
    if word.length() > k, there is a kth character and you can jut return it
    else, generate a new string with all letters incremented in ascii value
        add the two strings together and recurse

    just use (c == 'z') ? 'a' : c+1 for each letter c in word to increment each letter by 1
    handles the case where c == 'z' by looping back to 'a'

runtime: O(k)
    starting at word.length() == 1, we continue to build the string by doubling the string size until it equals to k or more
    1 + 2 + 4 + 8 ..... + k = (2k - 1) ish
    geometric progression sums to O(k)

space: O(k)
    word will hold around k characters at most at a given time
*/

#include <iostream>
using namespace std;

char buildString(string word, int k) {
    if (word.length() >= k) {
        return word[k-1];
    }

    string newStr = "";
    for (char c : word) {
        newStr += (c == 'z') ? 'a' : c+1;
    }
    
    return buildString(word + newStr, k);
}

char kthCharacter(int k) {
    return buildString("a", k);
}

// int main() {
//     cout << kthCharacter(5) << endl;
//     return 0;
// }