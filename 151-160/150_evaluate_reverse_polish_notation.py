
from typing import List

"""
150. Evaluate Reverse Polish Notation (https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

annoying things about this problem:
    1. do NOT use the isnumeric function since this function doesn't return true for negative numbers
        "The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False."
    2. do NOT use floor division to truncate to zero
        python floor divison always rounds downwards, NOT towards zero
        this means that negative numbers get even more negative when rounding down
        example: 6/-132 = -0.45454545...
            python floor division rounds down to -1
            truncate to zero truncates to 0 

this problem calls for the use of a last in first out stack
    this is because the last two integers are always the first two to be operated on
    ex. tokens = ["4","13","5","/","+"]
        stack of numbers = [4, 13, 5]
        apply the first operation to the last two numbers -> 13/5 = 2.6 -> add to the stack
        stack of numbers = [4, 2.6]
        apply the second operation to the last two numbers -> 4+2.6 = 6.6
    this is pretty much how the reverse polish notation works

algorithm:
    1. iterate through each token in tokens
    2. if tokens[i] is a number, add it to the top of the stack
    3. if tokens[i] is an operation, perform that operation with the top two elements in the stack
    4. continue until the stack is the result

runtime: O(n)
space: O(n)
"""


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token.lstrip("-").isdigit():
            stack.append(int(token))
            continue
        n1 = stack.pop()
        n2 = stack.pop()
        if token == "+":
            stack.append(n2 + n1)
        elif token == "-":
            stack.append(n2 - n1)
        elif token == "*":
            stack.append(n2 * n1)
        elif token == "/":
            stack.append(int(n2 / n1))
    return stack[0]