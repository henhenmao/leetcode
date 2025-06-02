
import java.util.ArrayList;

/*
2094. Finding 3-Digit Even Numbers (https://leetcode.com/problems/finding-3-digit-even-numbers/description/?envType=daily-question&envId=2025-05-12)


rules: 
    - The integer consists of the concatenation of three elements from digits in any arbitrary order.
    - The integer does not have leading zeros.
    - The integer is even.

- keep in mind that digits can contain duplicates

for this question, you just need to get all combinations of the digits that happen to be even numbers
    - we can just have three for loops that loop through each digit
        - the last for loop can increment in twos so only the even numbers are considered at all
    - after using a number, we add it back so it can be reused sometime else
        - this also lets us use each duplicate number at most once for each duplicate

algorithm:
    1. create an array d of size 10 that will contain the frequency of each digit 0-9
    2. have three for loop, each representing the hundreds place, tens place, and ones place
        make the third for loop increment in twos so only even numbers
    3. for each digit j that a for loop tries, id d[j] == 0, cannot use that number since it either doesn't exist or is already being used
        if digit j is used, subtract d[j] by 1 and continue to the deeper for loops
    4. for each even number that makes it to the end of the third for loop, we know that it is a valid combination to be returned
        we can add the number to the result
    5. once a for loop is done with a digit and is ready to move onto the next one, increase d[j] by 1 so it returns to its original value
        this allows for other for loops to use digit[j] since the current for loop isn't using it anymore

runtime: O(1) number of digits that can be used is constant,
    first loop: 9, second loop: 10, third loop: 5
    O(450) -> O(1)
space: O(1)
*/


class Solution {
    public int[] findEvenNumbers(int[] digits) {

        // creating an array of all possible digits
        // only incrementing ones that exist in the array digits
        int[] d = new int[10];
        for (int digit : digits) {
            d[digit]++;
        }

        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 1; i < d.length; i++) {
            if (d[i] == 0) continue; // skip digits that don't exist
            d[i]--;
            for (int j = 0; j < d.length; j++) {
                if (d[j] == 0) continue; // skip
                d[j]--;
                for (int k = 0; k < d.length; k+=2) { // incrementing by 2 so only even numbers are considered
                    if (d[k] == 0) continue;
                    res.add(i*100 + j*10 + k);
                }
                d[j]++;
            }
            d[i]++; // kind of like backtracking
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}