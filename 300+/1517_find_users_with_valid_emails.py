
import pandas as pd

"""
1517. Find Users With Valid E-Mails (https://leetcode.com/problems/find-users-with-valid-e-mails/description/)

create a function that takes in an email string and returns a boolean on whether or not that email is valid
checks 
    - first character is a letter
    - all characters excluding characters part of the domain are either letters, digits, or in ['-', '_', '.']
    - string ends with the leetcode email domain

apply this function onto the users table 

runtime: O(n)
space: O(n)
"""

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    domain = '@leetcode.com'
    def isValid(mail):
        if not mail[0].isalpha():
            return False
        for i in range(0, len(mail)-len(domain)):
            if not mail[i].isalnum() and mail[i] not in ['-', '_', '.']:
                return False
        if not mail.endswith(domain):
            return False
        return True

    users = users[users['mail'].apply(isValid)]
    return users



