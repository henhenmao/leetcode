
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""
133. Clone Graph (https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=oizxjoit)
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

shallow copy vs deep copy:
    shallow copy:
        a shallow copy creates a new object but does not duplicate any nested objects
        instead, they create references to the nested objects' memory locations
        ex. a = [1,2,3]
            b = copy.copy(a) # shallow copy
            print(id(a)) -> 123
            print(id(b)) -> 124
            the object of the list itself will have a different memory location

            print(id(a[0])) -> 125
            print(id(b[0])) -> 125
            inner elements of the list will have the same memory locations since b references memory of elements of a

    deep copy:
        creates an independent new copy of the original object, including all nested objects
            a = [1,2,3]
            b = copy.deepcopy(a) # deep copy
            print(id(a)) -> 123
            print(id(b)) -> 124

            print(id(a[0])) -> 125
            print(id(b[0])) -> 126

wow isn't this just amazing

notes for this question:
    - all nodes can be accessed from the starting node
    - each node has a unique value
    - no repeating edges or self loops

how to make a graph:
    - create each node
    - for each node add a path from it to each of its neighbors

algorithm:
    1. starting from the reference node, create a copy of the node and mark the node in the visited hashmap
    2. check all of the neighbors of the current node
    3. if the neighbor has been visited before, we know the copy node has been created, so add a path from the current copy to the neighbor copy
    4. recursively call the previous steps onto all neighbors of nodes
    5. stop recursion when all nodes have been visited

runtime: O(E+V) E = number of edges in graph and V = number of vertices in the graph
space: O(E+V)
"""

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    visited = {}
    def dfs(curr):
        # base case
        if curr in visited:
            return visited[curr]
        
        if not curr:
            return None

        # creates a new copy of the current node
        copy = Node(curr.val)
        visited[curr] = copy

        # recursively call the cloning function
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs(neighbor))
        return copy

    return dfs(node)