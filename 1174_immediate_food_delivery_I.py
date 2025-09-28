
import pandas as pd


"""
1174. Immediate Food Delivery I (https://leetcode.com/problems/immediate-food-delivery-ii/description/)

getting all first orders:
get all of the first orders by taking the minimum of the groupby of each customer_id
merge first orders and delivery on the customer id and order date so that table remains with only the first orders

getting percentage of immediate orders
return the percentage of rows where the order date is the same as the customer prefered delivery date

runtime: O(n)
space: O(n)
"""

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    customers = delivery['customer_id'].nunique()
    first_orders = delivery.groupby('customer_id')['order_date'].min()
    df = pd.merge(delivery, first_orders, on=['customer_id', 'order_date'])
    percentage = ((df['order_date'] == df['customer_pref_delivery_date']).sum()/customers*100).round(2)
    return pd.DataFrame({'immediate_percentage': [percentage]})
