

/* 
11. Container With Most Water (https://leetcode.com/problems/container-with-most-water/)

things to note:
    given two points in the container heights[i] and heights[j], where j > i,
    the area of water between the two points can be calculated as (j-i) * (Math.min(heights[i], heights[j]))
    since (j-i) is the length and (Math.min(heights[i], heights[j])) is the shared height between the two

algorithm:
    use two pointers and position one at the left and one at the right (l and r)
    constantly check that the area between the two pointers is greater than any area
    compare heights[l] and heights[r] and move the pointer with less height
    this will ensure that you are always checking for the highest possible height
    given your limited control over the length of the area. (which always goes down by 1 every time you move a pointer)

runtime: O(n) since the two pointers travel once until they meet in the middle
space: O(1)

*/

class Solution {
    public int maxArea(int[] height) {

        // setting pointers in left and right
        int l = 0;
        int r = height.length-1;

        int area = 0;
        int temp = 0;

        while (l < r) {

            // getting current area between l and r pointers and comparing to max height
            temp = (r-l) * Math.min(height[l], height[r]);
            if (temp > area) {
                area = temp;
            }

            // moving the most optimal pointer to move
            if (height[l] >= height[r]) {
                r -= 1;
            } else {
                l += 1;
            }
        }
        return area;
    }
}