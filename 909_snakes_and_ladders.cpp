


/*
909. Snakes and Ladders (https://leetcode.com/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150)

main issue with this problem is that the board is in a Boustrophedon style, like in an actual snakes and ladders board

a boustrophedon style board is one that alternates in direction at each row
    starting at the bottom left cell of the board, we go from left to right on the first row
    when we make it up to the second row, we go from right to left instead

once we figure out a system to navigate the board in the boustrophedon style, rest of the question should be fairly simple
the direction you are in depends on the row
    if you are on row [n-1], you will be travelling left to right
    if you are on row [n-2], you will be travelling right to left
    if you are on row [n-3], you will be travelling left to right again

one solution is to keep count of which row you are in
if you are on the first row, travel from left to right
    every time you go up a row, chenge your direction

this is actually a problem when we introduce snakes and ladders
since we can go up multiple rows at a time
need a function that can do the following:
    given an integer value curr between 1 and n^2, be able to calculate
    1. the board position containing square curr
    2. also the direction you are going in

remember that the board is always n * n

getting row:
    (curr-1)/n will always return the number of rows the current cell is away from the last row
    ex. square 6 -> (6-1)/6 = 0 rows away from the last row -> row n-1
    ex2. square 15 -> (14/6) = 2 rows away from the last row  -> row n-3

getting col:
    first assume that the board is not boustrophedon style and goes left to right in all rows
    (curr-1)%n will return the zero indexed column number
    with the boustrophedon stlye in mind, we can use the row number to check which direction the row goes
    if left -> right:
        column number is just (curr-1)%n
    if right-> left:
        column number is n - (curr-1)%n

knowing which direction:
    if (n-1 - row number) is an even number, you are in a left -> right row
    if odd number, go other way


runtime: O(n^2)
space: O(n^2)
*/


#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// getPosition takes in a square number on the snakes and ladders board and also the board size 
// returns the row and column number of the square number given the fact that the board is boustrephedon style
vector<int> getPosition(int n, int curr) {
    vector<int> position;
    int row = n-1-(curr-1)/n;
    int col;
    if ((n-1-row) % 2 == 0) {
        col = (curr-1)%n;
    } else {
        col = n - (curr-1)%n - 1;
    }
    // cout << "square " << curr << " is at row " << row << " and col " << col << endl;
    position.push_back(row);
    position.push_back(col);
    return position;
}

int snakesAndLadders(vector<vector<int>>& board) {
    int n = board.size();
    vector<int> minrolls(n*n+1, -1);
    queue<int> queue;
    minrolls[1] = 0; 
    queue.push(1);

    while (!queue.empty()) {
        int curr = queue.front();
        queue.pop();

        for (int i = 1; i <= 6 && curr+i <= n*n; i++) {
            vector<int> nextSquare = getPosition(n, curr+i);
            int v = board[nextSquare[0]][nextSquare[1]];
            int y = v > 0 ? v : curr+i;

            if (y == n*n) {
                return minrolls[curr]+1;
            }

            if (minrolls[y] == -1) {
                minrolls[y] = minrolls[curr]+1;
                queue.push(y);
            }
        }
    }

    return -1;
}

// int main() {
//     vector<vector<int>> board = {{-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1},{-1,-1,-1,-1,-1,-1},{-1,35,-1,-1,13,-1},{-1,-1,-1,-1,-1,-1},{-1,15,-1,-1,-1,-1}};
//     cout << snakesAndLadders(board) << endl;

//     return 0;
// }