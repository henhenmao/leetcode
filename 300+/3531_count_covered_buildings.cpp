


/*
3531. Count Covered Buildings (https://leetcode.com/problems/count-covered-buildings/?envType=daily-question&envId=2025-12-15)

covered building = building with a building somewhere in each four directions

for a given row on the grid, only considering the x axis, all buildings that are not the leftmost or rightmost building are "covered" in that one row
we can apply this same logic on each column, with each building that isn't the topmost or bottommost are "covered" for that column

therefore, we can conclude that for each building, as long as it is not a leftmost, rightmost, topmost, or bottommost building on any row or column, it is covered

to solve this problem, we can simply store for each row and column, the far extremes
    have two hashmaps, one for rows and one for columns

    xMap = {leftmost position, rightmost position}
    yMap = {topmost position, bottommost posistion}


when we loop over each building position, we check the following: let x = buildings[i][0] and x = buildings[i][1]
    is x in xMap[y] - this checks if the x is in leftmost or rightmost position
    if y in yMap[x] - this checks if the y is in topmost or bottommost position

    if neither of these conditions are true, the building is covered

runtime: O(n)
space: O(n)
*/

#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int countCoveredBuildings(int n, vector<vector<int>>& buildings) {  
    int numBuildings = buildings.size();
    if (n < 3 || numBuildings < 5) return 0;

    unordered_map<int, pair<int, int>> xMap;
    unordered_map<int, pair<int, int>> yMap;

    // rows
    for (auto& building : buildings) {
        int row = building[0], col = building[1];

        if (xMap.count(col) == 0) {
            xMap[col] = {row, row};
        } else {
            xMap[col].first = min(xMap[col].first, row);
            xMap[col].second = max(xMap[col].second, row);
        }
        
        if (yMap.count(row) == 0) {
            yMap[row] = {col, col};
        } else {
            yMap[row].first = min(yMap[row].first, col);
            yMap[row].second = max(yMap[row].second, col);
        }
    }

    int res = 0;

    // for each building, check if conditions are met
    for (auto& building : buildings) {
        int row = building[0], col = building[1];

        if (xMap[col].first == row || xMap[col].second == row) continue;
        if (yMap[row].first == col || yMap[row].second == col) continue;

        res += 1;
    }

    return res;
}

int main() {
    // int n = 3;
    // vector<vector<int>> buildings = {{1,2}, {2,2}, {3,2}, {2,1}, {2,3}};

    int n = 5;
    vector<vector<int>> buildings = {{1,3}, {3,2}, {3,3}, {3,5}, {5,3}};

    cout << countCoveredBuildings(n, buildings) << endl;
    return 0;
}