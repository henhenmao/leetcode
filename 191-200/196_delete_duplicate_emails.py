
import pandas as pd

"""
196. Delete Duplicate Emails (https://leetcode.com/problems/delete-duplicate-emails/)

pandas drop_duplicates removes all duplicates, by default keeping the first occurence of a row
since we want to keep the email with the smallest id, and ids can be out of order, we sort the database by the id column prior

runtime: O(n logn)
space: O(1) - database modified in place
"""


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by=['id'], inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)
