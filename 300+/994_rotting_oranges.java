
import java.util.Queue;
import java.util.LinkedList;

/*
994. Rotting Oranges (https://leetcode.com/problems/rotting-oranges/description/)

this is a classic breadth first search question


algorithm:
    1. find all of the initally rotten oranges and place them all in a queue
    2. while the queue is not empty: simulate a "day" passing
        take size = queue.size() and pop the first size oranges from the queue as you add adjacent oranges to the queue
    3. after you have looped through the first size oranges, you know all new oranges in the queue are ones that are rotten on the next day
    4. continue these steps until the queue is empty

runtime: O(n * m)
space: O(n * m)
*/






class Solution {
    public int orangesRotting(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] visited = grid;
        int[][] directions = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};

        Queue<int[]> queue = new LinkedList<>();
        int count = 0;
        int oranges = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[] {i, j});
                    visited[i][j] = 0;
                } else if (grid[i][j] == 1) {
                    oranges += 1;
                }
            }
        }

        while (oranges > 0 && !queue.isEmpty()) {
            int size = queue.size();
            for (int a = 0; a < size; a++) {
                int[] curr = queue.poll();
                int i = curr[0];
                int j = curr[1];
                for (int[] d : directions) {
                    int nexti = i + d[0];
                    int nextj = j + d[1];
                    if (nexti < 0 || nexti >= n || 
                        nextj < 0 || nextj >= m || 
                        visited[nexti][nextj] == 0) {
                        continue;
                    }
                    queue.offer(new int[] {nexti, nextj});
                    visited[nexti][nextj] = 0;
                    oranges -= 1;
                }
            }
            count += 1;
        }

        if (oranges == 0) {
            return count;
        }
        return -1;
    }
}