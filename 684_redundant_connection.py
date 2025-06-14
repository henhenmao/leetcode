

from typing import List

"""
684. Redundant Connection (https://leetcode.com/problems/redundant-connection/description/)

we are given a graph that was initially a tree with n nodes labelled 1 to n
one additional edge was added between two different nodes chosen form 1 to n, and was not an edge that already existed
    this essentially creates a cycle in the tree somewhere

we need to find this cycle, find all edges in the cycle, and return the edge in the cycle that appears last in the input

we can use a union find like algorithm to do this
    iterate through the edges to build a graph
    keep track of the parent root node of the graph
    if an edge connect two nodes with sharing parent nodes, then that is your cycle

algorithm:
    1. set parent array where parent[i] is the parent node of node i
    2. set rank array 
    3. create a find function
        find takes in any node and keeps updating the node to its parent node until the current node equals the parent node
        this will find the parent node of any connected component
    4. create a union function
        union takes in any two nodes and merges them together 
        uses the find function to find the parent nodes of each node and get the size of the corresponding parent node's connected component
        merges the smaller connected component to the larger one
    5. attempt to merge the nodes between each edge in edges array
    6. if the two nodes in an edge share the same parent node, we know that the edge completes a cycle, so set res to the edge 

runtime: O(V + E) where V is the number of vertices and E is the number of edges
space: O(V + E)
"""

def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    parent = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        res = node
        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]
        return res
    
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return
        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return
    
    res = -1
    for edge in edges:
        n1, n2 = edge[0]-1, edge[1]-1 # subtract by one since input is 1-indexed
        if find(n1) == find(n2):
            res = edge
        union(n1, n2)
    return res

# edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
# print(findRedundantConnection(edges))
