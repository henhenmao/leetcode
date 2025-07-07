

/*
228. Summary Ranges (https://leetcode.com/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150)

nums is sorted in ascending order and contains unique values
each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
ranges are inclusive of a and b

basically just iterate over the array of nums and keep going until there is a gap between two adjacent numbers
gap means a difference of more than 1

algorithm:
    1. return empty vector nums is empty (important!!)
    2. keep track of the index of start of your current range (starting at 0)
    3. iterate through nums starting i=1 and do nothing until nums[i] and nums[i-1] have a gap between them
        check if nums[i]-nums[i-1] != 1 for a difference of more than 1 between two adjacent numbers
        need to convert to long when evaluating since values can be very big
    4. when gap is found between nums[i] and nums[i-1], you know the range ends at index i-1
        add range of nums[start] -> nums[i-1] to the result
    5. since the loop only checks differences between nums[i] and nums[i-1], the last interval will not be counted in the loop
        manually add the last interval 
        distinguish between the interval of "a->b" and "a" by checking if start index == nums.size()

runtime: O(n) where n is the size of nums
space: O(n)
*/


#include <iostream>
#include <vector>
using namespace std;


vector<string> summaryRanges(vector<int>& nums) {
    vector<string> res;

    if (nums.size() == 0) {
        return res;
    }

    int start = 0; // index of the start of current range
    // adds everything except for the last interval
    for (int i = 1; i < nums.size(); i++) {
        if ((long) nums[i]- (long) nums[i-1] != 1) {
            if (start == i-1) {
                res.push_back(to_string(nums[start]));
            } else {
                res.push_back(to_string(nums[start]) + "->" + to_string(nums[i-1]));
            }
            start = i;
        }
    }

    // adding the last range
    if (start == nums.size()-1) {
        res.push_back(to_string(nums[start]));
    } else {
        res.push_back(to_string(nums[start]) + "->" + to_string(nums[nums.size()-1]));
    }

    return res;
}


int main() {
    vector<int> nums = {-2147483648,0,2,3,4,6,8,9};
    vector<string> res = summaryRanges(nums);
    for (string s : res) {
        cout << s << " ";
    } 
    cout << endl;
    return 0;
}