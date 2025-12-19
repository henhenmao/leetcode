

import pandas as pd

"""
1393. Capital Gain/Loss (https://leetcode.com/problems/capital-gainloss/description/)

create a new column in the Stocks table that depending on the operation, gives a positive or negative integer gain
    use pandas apply rowwise axis=1 to do this
    buy = loss of money
    sell = gain of money

once you have a gain loss column with positive and negative integers representing a gain or loss
    grouping by the stock name, get the total capital gain loss of each stock

filter out the proper columns

runtime: O(n)
space: O(n)
"""

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    def gainloss(row):
        if row['operation'] == 'Buy':
            return -1 * row['price']
        return row['price']

    stocks['capital_gain_loss'] = stocks.apply(gainloss, axis=1)
    stocks = stocks.groupby(by='stock_name', as_index=False).sum()
    return stocks[['stock_name', 'capital_gain_loss']]