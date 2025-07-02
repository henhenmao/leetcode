
/*
299. Bulls and Cows (https://leetcode.com/problems/bulls-and-cows/description/)

the main issue with this problem is the fact that secret and guess can have duplicate digits
ex. secret = "1123", guess = "0111"
output = "1A1B"
the "1" in index 1 on secret and guess match as a bull, and either the second or third "1" matches to be a cow
but the cow is only matched once since there are only two "1"s in secret

because of this, we should keep track of the frequency of each character in secret using a hash table
decrement the value of any characters we come across
if we come across a character that matches but has a value of 0 in the map, we can ignore ir

ex. secret = "1123", guess = "0111"
    freq = {"1":2, "2":1, "3":1}

    iterate over each character in both strings
    1. check if guess[i] exists in secret (can just check if key exists in freq)
    2. if exists, check if frequency == 0 in map, if true, continue
    3. if frequency > 0, check if a bull or cow
    4. decrement frequency for value in map

edge case (kinda):
    secret = "1122", guess = "1222"
    the "2" in index 1 of guess will match as a cow before the other two "2"s
    although in the intended output the last two "2"s get matches as bulls with no cows

    to fix this i'll just do two separate passes, the first only looking for bulls
    the second pass will work as usual
    this will let us prioritize the existence of bulls over cows
    also have a visited array to make sure we don't repeat values from the first pass in the seocnd pass

runtime: O(n) where n is the length of guess = length of secret
space: O(n)
*/


#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

string getHint(string secret, string guess) {

    // result variables
    int a = 0;
    int b = 0;

    int n = secret.length();
    unordered_map<char, int> freq;
    vector<bool> visited(n, false);

    // creating hashmap of frequency of each chraracter in secret
    for (char c : secret) {
        freq[c]++;
    } 

    // first pass: prioritize bulls
    for (int i = 0; i < n; i++) {
        if (freq.count(guess[i]) && freq[guess[i]] > 0 && guess[i] == secret[i]) {
            a++;
            freq[guess[i]]--;
            visited[i] = true;
        }
    }

    // loop through indexes of secret and guess to find matches
    for (int i = 0; i < n; i++) {
        if (freq.count(guess[i]) && freq[guess[i]] > 0 && !visited[i]) {
            
            // check if current index is a bull or a cow
            if (guess[i] == secret[i]) { // is a bull
                a++;
            } else {
                b++;
            }

            freq[guess[i]]--;
        }
    }
    return to_string(a) + 'A' + to_string(b) + 'B';
}

int main() {
    string secret = "1122";
    string guess = "1222";
    cout << getHint(secret, guess);
    return 0;
}


