

/*
904. Fruit Into Baskets (https://leetcode.com/problems/fruit-into-baskets/description/?envType=daily-question&envId=2025-08-04)

sliding window problem

have a left and right pointer to make a window
all fruits within the window from left to right represents the current total fruits in the two baskets
keep incrementing right pointer to try to get as many fruits as possible
    when three different types of fruit exist in the window, increment the right pointer until the window is valid again

algorithm:
    1. make left and right pointers staritng at index 0 for sliding window
    2. increment the current fruit at the right pointer to types[fruits[right]]++
        if the fruit doesn't exist in types, create it and set it to 1
    3. check if the current window is invalid:
        keep track of the distinct types of fruits that exist in the window
            if types.size() == 3, there are three distinct fruit types in the window, and is invalid
            if invalid: decrement the value of types[fruits[left]] (we know that the key will exist since it was added by right pointer)
                if a decrement turns types[fruits[left]] == 0, erase the key value pair
    4. as long as the resulting window only contains two distinct fruit types, get the size of the window
        update the max window size seen so far

runtime: O(n) where n is the size of fruits
space: O(n)
*/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int totalFruit(vector<int>& fruits) {
    int left = 0;
    int right = 0;
    int maxFruits = 0;
    int currFruits = 0;

    unordered_map<int, int> types;
    
    
    while (right < fruits.size()) {

        types[fruits[right]]++;

        while (types.size() >= 3) {
            types[fruits[left]]--;
            if (types[fruits[left]] == 0) {
                types.erase(fruits[left]);
            }
            left++;
        }

        maxFruits = max(maxFruits, right-left+1);
        right++;


    }
    return maxFruits;
}


int main() {
    vector<int> nums = {1, 2, 1};

    cout << totalFruit(nums) << endl;

    return 0;
}