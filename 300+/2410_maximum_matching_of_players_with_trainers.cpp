

/*
2410. Maximum Matching of Players With Trainers (https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/?envType=daily-question&envId=2025-07-13)
Note: This question is the same as 445: Assign Cookies

just sort both the player array and the trainer array in non-decreasing order
put two pointers at the start of each array, let i be the pointer on players and j be the pointer on trainers
greedily match the minimum possible player and the minimum possible trainer if possible
if you can match player[i] and trainer[j], add 1 to the total match and increment both i and j
if you cannot match player[i] and trainer[j], just increment j
    we don't need to worry about trainer[j] since we know they cannot train anybody (players are in non-decreasing order) 

runtime: O(n * log(n) + n * log(m)) where n is the length of players and m is the length of trainers, sorted both arrays
space: O(1)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
    sort(players.begin(), players.end());
    sort(trainers.begin(), trainers.end());

    int i = 0;
    int j = 0;
    int matches = 0;

    while (i < players.size() && j < trainers.size()) {
        if (players[i] <= trainers[j]) { // current trainer can train the current player
            matches++;
            i++;
        }
        j++;
    }
    
    return matches;
}


int main() {
    return 0;
}