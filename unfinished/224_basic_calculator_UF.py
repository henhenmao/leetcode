


"""
224. Basic Calculator (https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150)
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid)

create a function solve that takes in a string without parentheses and evaluates/returns the integer value
    since there is no multiplication or division in the calculator, do not need to worry about order
        just iterate from left to right

find all pairs of parentheses
    use a stack to find correct pairs of parentheseses
    starting from the innermost parentheses, evaluate solve on the contents inside
    replace the parentheses expression with the evaluated answer
        repeat with recursion

ex. s = "(1+(4+5+2)-3)+(6+8)"
    1. use stack to find first pair of parentheses
        curr = "(1+(4+5+2)-3)"
    2. remove the outer parentheses and recurse into expression
        curr = "1+(4+5+2)-3"
    
    s = "1+(4+5+2)-3"
    3. use stack to find first pair of parentheses
        curr = "(4+5+2)"
    4. remove the outer parentheses and recurse into expression
        curr = "4+5+2"
    
    s = "4+5+2"
    6. use a stack to find first pair of parentheses
    7. if no parentheses exist, solve the expression from left to right
    8. return the evalutated answer

"""

# assumes that s contains no parentheses
def solve(s):
    pass

def calculate(s: str) -> int:
    pass
    # apply calculate recursively on each pair of parentheses





