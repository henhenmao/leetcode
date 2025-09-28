


/*
3005. Count Elements With Maximum Frequency (https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2025-09-17)

get the frequency of each distinct integer in nums
iterate over the frequency map to get the max frequency, while counting the number of distinct keys with the same max frequency


*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


int maxFrequencyElements(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int n : nums) {
        freq[n]++;
    }

    int maxFreq = 0;
    int numOccurences = 0;
    for (const auto& pair : freq) {
        if (pair.second > maxFreq) {
            numOccurences = 1;
            maxFreq = pair.second;
        } else if (pair.second == maxFreq) {
            numOccurences++;
        }
    }
    return maxFreq * numOccurences;
}

int main() {



    return 0;
}