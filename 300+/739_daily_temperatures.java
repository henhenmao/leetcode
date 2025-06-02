
import java.util.Stack;

/*
739. Daily Temperatures (https://leetcode.com/problems/daily-temperatures/)

we can use a last in first out stack to solve this question
after some thinking we can realize that you always need to keep track of the lowest temperature so far

algorithm:
    1. create lifo stack
    2. iterate through all temperatures[i] in temperatures
    3. if the stack is not empty, check if the temperature at the top of the stack is less than temperatures[i]
        proceed to keep popping from the top of the stack until the top of the stack has a temperature larger than the current one
        add the difference in indices to the result, (i - stack.pop()) as it is the number of days you have to wait
        after the (stack.pop())th day to get a warmer temperature on the ith day
    4. if stack is empty, add i to the stack

runtime: O(n) each temperature is iterated once through
space: O(n) stack
 */

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.empty() && temperatures[stack.peek()] < temperatures[i]) {
                res[stack.peek()] = i - stack.pop();
            }
            stack.push(i);
        }

        return res;
    }
}