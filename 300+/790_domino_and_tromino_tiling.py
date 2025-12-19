

"""
790. Domino and Tromino Tiling (https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=problem-list-v2&envId=dynamic-programming)

we are given 3 general options
    1. place a vertical domino (shrinks n by 1)
    2. place two horizontal dominos side by side (shrinks n by 2)
    3. place two trominos side by side (shrinks n by 3)

key idea: above tile combos aren't just side by side
    ex. a tromino placed at the start of the grid can have as many horizontal dominos after it
        as long as the trimono is finally resolved by another tromino at some point in the end

if n == 1
    can only place vertical domino
if n == 2
    can place two vertical dominos
    can place two horizontal dominos
if n == 3
    can place three vertical dominos
    can place two horizontal dominos + one vertical domino (x2)
    can place two trimonos (x2)
if n == 4:
    can place four vertical dominos
    can place four horizontal dominos
    two horizontal dominos + two vertical (x3)
    two trominos + one horizontal domino (x2)
    two trominos + one vertical (x4)

we can divide the 2*n grid into these subproblems
    each subproblem must resolve into a 2*m rectangular shape that fits into the grid

domino rules
    - can place a vertical if and only if n >= 1 and the board is resolved (shrinks n by 1)
    - double horizontals can be placed only if n >= 2 and the board is resolved (shrinks n by 2)

tromino rules
    - will define the board as "unresolved" if there is a placed tromino without a second tromino to complement it
    - tromonos can only be placed as long as n >= 3
    - first placed tromino essentially shrinks n by 1 but leaves the grid "unresolved"
        - each placed trimono must be resolved by another tromino
        - only horizontal dominos can be placed when a tromino is unresolved
            - to ensure there is room for a tromino at the end, horizontal dominos may only be placed as long as n >= 3
            - if board is still unresolved with n == 2, only possible move is to place a tromino
        - every tromino pair possibility has a symmetrical possibility (multiply tromino recursion totals by two)

runtime: O(n)
space: O(n)
"""

def numTilings(n: int) -> int:

    dp = [[-1] * (n+1) for _ in range(2)]
    mod = 10**9 + 7

    def recur(n, resolved):
        nonlocal dp

        if n == 0: # only count if still resolved
            return resolved
        
        if n < 0:
            return 0

        if dp[resolved][n] != -1:
            return dp[resolved][n]

        total = 0
        if resolved:
            total = (total + recur(n-1, True)) % mod # placing one vertical
            total = (total + recur(n-2, True)) % mod # placing two horizontal
            total = (total + 2 * recur(n-2, False)) % mod # placing a tromino



        else:
            total = (total + recur(n-1, False)) % mod # placing a horizontal
            total = (total + recur(n-1, True)) % mod # resolving with second tromino

        dp[resolved][n] = total
        return total

    return recur(n, True)

n = 30
print(numTilings(n))