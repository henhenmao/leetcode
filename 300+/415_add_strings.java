

/*
415. Add Strings (https://leetcode.com/problems/add-strings/description/)

i believe i may have to to the addition inside of the string
start at the back of each string and add and keep track of the carry

note: whenever you are converting java digit characters to strings
    for example, when trying to convert the character c ='5' to an integer 5
        (int)(c) does NOT convert the string to 5, instead converts to the ASCII value of '5', which is 53
        to fix this problem, subtract all integer conversions by the base ASCII value of '0', which is 48
        (int)(c) - "0" = 53 - 48 = 5

do the same thing as 2. Add Two Numbers (https://leetcode.com/problems/add-two-numbers/description/)

algorithm:
    1. have two pointers p1 and p2 at the end of each num1 and num2 and initialize a variable for the carry
    2. add num[p1] and num[p2] and the carry together for a total sum
    3. get the digit representation by modding by 10
    4. get the carry by dividing by 10
    5. decrement p1 and p2
    6. return the reversed result string since you started in the ones place

runtime: O(max(n, m)) where n is the length of num1 and m is the length of num2
space: O(max(n, m)) 
*/

class Solution {
    public static String addStrings(String num1, String num2) {
        
        int l1 = num1.length();
        int l2 = num2.length();
        int p1 = l1-1;
        int p2 = l2-1;
        int carry = 0;

        StringBuilder res = new StringBuilder();

        while (p1 >= 0 || p2 >= 0 || carry > 0) {
            // adding what you have
            int total = carry;
            if (p1 >= 0) {
                // System.out.println(num1.charAt(p1));
                total += (int) (num1.charAt(p1)) - '0';
                p1 -= 1;
            }

            if (p2 >= 0) {
                total += (int) num2.charAt(p2) - '0';
                p2 -= 1;
            }

            // setting new carry and digit to add to result
            int digit = total % 10;
            carry = (int)(total / 10); 
            res.append(digit);
        }

        return res.reverse().toString();
    }
}
