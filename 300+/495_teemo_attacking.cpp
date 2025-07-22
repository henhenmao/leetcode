

/*
495. Teemo Attacking (https://leetcode.com/problems/teemo-attacking/)

keep track of the start time and the end time of the poison at each attack that teemo makes on ashe

let int start = the start time of ashe's last or current poison
let int end = the end time of ashe's last or current poison

let int attack be the time that teemo attacks ashe
    if attack is greater than end, that means that teemo attacked ashe after her last poison ended
        because we know that these two poisons do not overlap, we can add (end-start+1) to the total time
            (end-start+1) is the total time of ashes last poison

    if attack is less than or equal to end, that means that teemo attacked ashe while she was already poisoned
        so we do not add anything to total time yet
        instead, we just update the end variable, essentially "resetting" the time of ashe's current poison
    
add (end-start+1) to the total time after the loop, since the loop does not include the last poison in the total time

runtime: O(n) where n is the length of timeSeries
space: O(1)
*/

#include <iostream>
#include <vector>
using namespace std;

int findPoisonedDuration(vector<int>& timeSeries, int duration) {
    
    int totalTime = 0;

    int start = -1;
    int end = -1;

    for (int attack: timeSeries) {

        if (attack > end) { // ashe is not already poisoned when teemo attacks
            totalTime += (end-start+1);
            start = attack;
        }
        end = attack + duration-1;
    }

    totalTime += (end-start);

    return totalTime;
}

int main() {
    vector<int> timeSeries = {1,4};
    int duration = 2;

    cout << findPoisonedDuration(timeSeries, duration) << endl;

    return 0;
}