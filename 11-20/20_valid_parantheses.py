


"""
20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/submissions/1649315539/)

this question requires a stack (it's pretty cool)

we can add as many opening parentheses as we want, as long as they become closed in the future at some point
we cannot add as many closing parentheses as we want, since a closing must have an opening

the solution to this problem is to add all opening parentheses to a stack, where the most recent opening parentheses is on top
    a closing parentheses will always close the most recent opening parentheses

we simple follow these rules:
    - if we encounter an opening bracket, we add it to the top of the stack
    - if we encounter a closing bracket: we must check it is valid
        - if stack is empty: not valid
        - if closing bracket does not match with the top of the stack: not valid

runtime: O(n), where n is the length of s
space: O(n)

"""

def isValid(s: str) -> bool:
        stack = []
        valid = {"(":")", "[":"]", "{":"}"}
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if len(stack) == 0 or valid[stack.pop()] != i:
                    return False
        return len(stack) == 0