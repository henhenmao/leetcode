


/*
135. Candy (https://leetcode.com/problems/candy/)

need to do two passes: front to back and back to front

find all adjacent rankings in one direction where ratings[i] > ratings[i-1]
find all adjacent rankings in the other direction where ratings[i-1] > ratings[i]

we can start with a vector of everyone's candies initially set with everyone getting one candy
we add more to someone's candies when they are neighboring someone with less ranking

first pass: front to back
    simply traverse i from start to end
    if ratings[i] > ratings[i-1]: set candies[i] to candies[i-1] + 1

    ex. ratings = [1,0,1,2,3]
    candies = [1,1,1,1,1] initially
    after first pass:
    candies = [1, 1, 2, 3, 4]

second pass: back to front
    traverse i from end to start
    if ratings[i-1] > ratings[i]:
        set candies[i-1] to either candies[i]+1 or candies[i-1]
    
    candies[i-1] might already greater than candies[i]+1 due to the first pass
    and we don't want to accidentally decrease the value

    so instead we set candies[i-1] to whatever is the max of candies[i]+1 and candies[i-1]


    ex. ratings = [1, 3, 2]
        first pass:
        candies = [1, 2, 1]
        second pass:
        ratings[1] > ratings[2] -> check that candies[1] = max(2, 2) = 2
        keep the max so we don't undo the previous work in the first pass

runtime: O(n)
space: O(n)
*/

#include <iostream>
#include <vector>
using namespace std;

int candy(vector<int>& ratings) {
    int count = 0;
    int n = ratings.size();
    vector<int> candies(n, 1); // setting each person's candies to 1 initially

    for (int i = 1; i < n; i++) {
        if (ratings[i] > ratings[i-1]) {
            candies[i] = candies[i-1] + 1;
        }
    }

    for (int i = n-1; i > 0; i--) {
        if (ratings[i-1] > ratings[i]) {
            candies[i-1] = max(candies[i-1], candies[i]+1);
        }
        count += candies[i-1];
    }

    return count + candies[n-1];
}


// int main() {
//     vector<int> ratings = {1,0,2};
//     cout << candy(ratings) << endl;
//     return 0;
// }

