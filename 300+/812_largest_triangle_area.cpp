


/*
812. Largest Triangle Area (https://leetcode.com/problems/largest-triangle-area/description/?envType=daily-question&envId=2025-09-27)

getting the area of three points of a triangle
    im pretty sure you just take the span of the x dimension (distance from the leftmost point to the rightmsot point)
    and then take the span of the y dimension (distance from the topmost point to the bottommost point)
    and the just imagine that as a rectange and divide by two

turns out i was wrong and stupid
    actual area of a traingle with three points is 
    A= (1/2) * |(​x1​(y2​−y3​) + x2​(y3​−y1​) + x3​(y1​−y2​))|

create a function that takes in three points and returns the area

since points.length is at most 50, we can jsut do a triple nested loop and try all combinations of triangle points

runtime: O(n^3) where n is the number of points
space: O(1)
*/


#include <iostream>
#include <vector>
using namespace std;



double getArea(vector<int>& a, vector<int>& b, vector<int>& c) {
    int ax = a[0], ay = a[1];
    int bx = b[0], by = b[1];
    int cx = c[0], cy = c[1];

    double area = (1.0/2) * abs((ax * (by-cy)) + (bx * (cy-ay)) + (cx * (ay-by)));
    return area;
}


double largestTriangleArea(vector<vector<int>>& points) {
    int n = points.size();
    double maxArea = 0;

    for (int i = 0; i < n; i++) {
        vector<int> a = points[i];
        for (int j = i+1; j < n; j++) {
            vector<int> b = points[j];
            for (int k = j+1; k < n; k++) {
                vector<int> c = points[k];
                maxArea = max(maxArea, getArea(a, b, c));
            }
        }
    }
    return maxArea;
}

int main() {
    // vector<vector<int>> points = {{0,0}, {0,1}, {1,0}, {0,2}, {2,0}};
    // vector<vector<int>> points = {{1,0}, {0,0}, {0,1}};

    vector<vector<int>> points = {{4,6}, {6,5}, {3,1}};
    cout << largestTriangleArea(points) << endl;
    return 0;
}