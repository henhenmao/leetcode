


/*
3477. Fruits Into Baskets II (https://leetcode.com/problems/fruits-into-baskets-ii/description/?envType=daily-question&envId=2025-08-05)

just going to do a greedy O(n^2) algorithm that for each fruits[i], searches the baskets from left to right
matches fruits[i] to the first baskets[j] greater than or equal to fruits[i]
mark baskets as full when a fruit is added, will need a separate array

*/

#include <iostream>
#include <vector>
using namespace std;

int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
    int n = fruits.size();
    int m = baskets.size();
    int unplaced = n;
    vector<bool> visited(m, false);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[j] && baskets[j] >= fruits[i]) {
                visited[j] = true;
                unplaced--;
                break;
            }
        }
    }
    return unplaced;
}

int main() {

    vector<int> fruits = {3,6,1};
    vector<int> baskets = {6,4,7};

    cout << numOfUnplacedFruits(fruits, baskets) << endl;

    return 0;
}