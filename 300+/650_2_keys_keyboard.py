

"""
650. 2 Keys Keyboard (https://leetcode.com/problems/2-keys-keyboard/?envType=problem-list-v2&envId=dynamic-programming)

two options
    1. copy all, replace clipboard, and increment total operations by 1
    2. add contents of the clipboard to the current string

let int s = length of the string of 'A' characters being typed
    int clipboard = length of the string 'A' characters in the clipboard
    int operations = number of operations made (either a copy all or a paste)
    
to avoid an infinite loop of copying, don't allow a copy if you have already copied
    you can check if your clipboard equals the current typed string to confirm whether or not you just copied
    
use a dp table to memoize the state (s, clipboard), initialize with n * n 2d matrix

i'm going to crash out

runtime: O(n^2)
space: O(n^2)

"""

def minSteps(n: int) -> int:
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    def typing(s, clipboard):
        # overshot target value n
        if s > n:
            return float("inf")
        
        if s == n:
            return 0
        
        if dp[s][clipboard] != -1:
            return dp[s][clipboard]
        
        res = float("inf")
    
        # paste
        if clipboard > 0:
            res = min(res, 1 + typing(s + clipboard, clipboard))

        # copy all 
        if s != clipboard: # avoids copying twice in a row
            res = min(res, 1 + typing(s, s))

        dp[s][clipboard] = res
        return res
    
    return typing(1, 0)
 
n = 11
print(minSteps(n))

        
    



