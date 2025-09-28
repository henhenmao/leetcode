

import pandas as pd

"""
586. Customer Placing the Largest Number of Orders (https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/)
Follow up: What if more than one customer has the largest number of orders, can you find all the customer_number in this case?

use value_counts to get the number of orders each different customer_number placed
get the max order count in the table
select only the rows that contain an order count equal to the max order count
filter out just the customer_number row

runtine: O(n)
space: O(n)
"""

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders['customer_number'].value_counts().reset_index()
    largest = counts['count'].max()
    counts = counts[counts['count'] == largest][['customer_number']]
    return counts
