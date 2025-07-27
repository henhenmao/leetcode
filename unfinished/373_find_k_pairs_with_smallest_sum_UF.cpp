

/*
373. Find K Pairs With Smallest Sum (https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150)

greedy minheap problem

convert both arrays into heaps 
take the smallest element from the top of each heap
    [1,7,11], [2,4,6] -> [1,2]
    pop the larger of the two
    1 < 2 -> [1,7,11], [4,6]

    iteration 2
    [1,7,11], [4,6] -> [1,4]
    1 < 4 -> [1,7,11], [6]

    iteration 3
    [1,7,11], [6] -> [1,6]
    1 < 6 -> [1,7,11], []

    if a heap becomes empty before k pairs have been created, take the first two elements in the non-empty heap

NEVRMIDN THIS DOES NOT WORK
*/

#include <iostream>
#include <vector>
#include <queue>
#include <functional> // for greater<int> comparator
using namespace std;

vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
    priority_queue<int, vector<int>, greater<int>> heap1(nums1.begin(), nums1.end());
    priority_queue<int, vector<int>, greater<int>> heap2(nums2.begin(), nums2.end());

    vector<vector<int>> res;

    while (!heap1.empty() && !heap2.empty() && k > 0) {
        int n1 = heap1.top();
        int n2 = heap2.top();

        if (n1 < n2) {
            heap2.pop();
        } else {
            heap1.pop();
        }

        vector<int> pair = {n1, n2};
        res.push_back(pair);
        k--;
    }

    return res;
}

int main() {
    vector<int> nums1 = {1,2,3,4,5,6,7,8,9};
    vector<int> nums2 = {2};
    int k = 4;
    vector<vector<int>> res = kSmallestPairs(nums1, nums2, k);

    for (vector<int> nums : res) {
        for (int n : nums) {
            cout << to_string(n) << " ";
        }
        cout << endl;
    }
}