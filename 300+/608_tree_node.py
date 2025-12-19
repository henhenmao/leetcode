
import pandas as pd

"""
608. Tree Node (https://leetcode.com/problems/tree-node/)

no parent = root node
no children = leaf node
else: inner node

create a function that checks the conditions and use pandas apply into a new row
create a set containing all parent nodes so that you get fast looup times when looking for parent nodes
apply the function onto each row of the table

runtime: O(n)
space: O(n)
"""

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    def getNode(row):
        if (pd.isna(row['p_id'])):
            return "Root"
        elif (row['id'] in parents):
            return "Inner"
        return "Leaf"

    parents = set(tree['p_id']) # fast lookup for each node in columns
    tree['type'] = tree.apply(getNode, axis=1) # apply across each row
    return tree[['id', 'type']]




