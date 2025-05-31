
import java.util.*;

/*
15. 3Sum (https://leetcode.com/problems/3sum/)

for Two Sum, we used a hashmap to find a single value that matched with another value
    we would add all values in nums to a hash set
    and then traverse nums again, checking if target-nums[i] exists in the hash

instead of a hashmap, we will use a two pointer technique

algorithm:
    1. sort the array (so we can use two pointers)
    2. for each value nums[i], set up two pointers at l = [i+1] and r = [nums.length-1]
    3. check if the sum if nums[i], nums[l], and nums[r] == 0
    4. if not, adjust the pointers based on the sum (recall that we sorted the array for this)

runtime: sorting = O(n * log(n)), two pointer inside for loop: O(n^2)
    total runtime = O(n^2), where n is length of nums
space: O(log(n)) - java sort

 */


class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>(); // creating a new 2d array that will contain output
        Arrays.sort(nums); // sorting nums so we can use two pointers

        for (int i = 0; i < nums.length-2; i++) { // nums.length >= 3
            if (i > 0 && nums[i] == nums[i-1]) {
                continue; // skip duplicate values for nums[i]
            }
            
            int l = i + 1;
            int r = nums.length-1;
            
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];

                if (sum == 0) { // if 0 sum: shift both l and r and add triplet to res
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l += 1;
                    r -= 1;

                    while (l < r && nums[l] == nums[l-1]) {
                        l += 1;
                    }
                } else if (sum > 0) { // if sum > 0: shift r to the left to decrease the sum
                    r -= 1;
                } else { // if sum < 0: shift l to the right ot increase the sum
                    l += 1;
                }
            }
        }
        return res;
    }
}