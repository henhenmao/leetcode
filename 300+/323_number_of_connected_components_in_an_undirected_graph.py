
from typing import List

"""
323. Number of Connected Components in an Undirected Graph (https://neetcode.io/problems/count-connected-components?list=blind75)
Locked behind a paywall on LeetCode but on Neetcode roadmap

i should attempt a graph traversal from every single node on the graph 
    each traversal will visit all connecting nodes and mark as visited
    every different successful traversal can be considered a separate component in the graph

algorithm:
    1. build an adjacency array with all nodes and the paths
    2. attempt a dfs traversal on each node from 0 to n
    3. all separate dfs traversals are a separate connected component in the graph

runtime: O(V + E) where V is the number of vertices and E is the number of edges
space: O(V + E) adjacency list
"""

def countComponents(n: int, edges: List[List[int]]) -> int:
    # create an adjacency matrix
    adj = [[] for _ in range(n)]

    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)


    visited = [False] * n
    # traverse every node in the graph with dfs
    def dfs(curr):
        for node in adj[curr]:
            if visited[node]:
                continue
            visited[node] = True
            dfs(node)
    
    res = 0
    for node in range(n):
        if visited[node]:
            continue
        visited[node] = True
        res += 1
        dfs(node)

    return res

"""
i'm going to do this problem again since i'm trying to learn what a union find algorithm is

union find:
    basically we want to keep track of the parent node of each connected component
    1. we can start off by assuming each node is a separate connected component and is a parent of itself
    2. we then can iterate over the edges array and connect connecting nodes by making them have the same parent
        ex. if node 0 is a parent of node 0 and node 1 is a parent of node 1 at the start
            and then we go over an edge of [0,1]
            we can make the parent of node 1 equal to the parent of node 0, which is node 0
            then if we find an edge of [1, 2]
            we can make the parent of node 2 equal to the parent of node 1, which is node 0 now

            we are essentially trying to make all connected nodes in a single component share the same parent

algorithm:
    1. set a parent array where parent[i] is the parent node of node i
    2. set a rank array where rank[i] is the size of the component where node i is the root (each node starts at 1)
    3. create a find function
        find takes in any node and keeps updating the node to its parent node until the current node equals the parent node
        this will find the parent node of any connected component
    4. create a union function
        union takes in any two nodes and merges them together 
        uses the find function to find the parent nodes of each node and get the size of the corresponding parent node's connected component
        merges the smaller connected component to the larger one
        return 1 if a successful union is performed else return 0
    5. attempt to merge the nodes between each edge in edges array
    6. every time a union is succesfully made we know subtract 1 from the result (res = n at the start)
        every time a union is made we know that node is a part of another component
        if a union is not made then we know there is a new connected component
        we are just counting the number of times a union is not made and returning the answer

runtime: O(V + E) where V is the number of vertices and E is the number of edges
space: O(V + E)
"""


def countComponents(n: int, edges: List[List[int]]) -> int:
    # keep track of parents and rank of each node
    parent = [i for i in range(n)]
    rank = [1] * n
    res = n # decrement res by 1 every time a union operation is made, res will contain the number of distinct parents at the end

    # find function find the root parent of curr
    def find(curr):
        res = curr
        while res != parent[res]:
            parent[res] = parent[parent[res]]
            res = parent[res]
        return res 
    
    # union compares two nodes and merges them together
    # taking into account which node's parent has a higher rank for optimization
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return 0

        if rank[p2] > rank[p1]:
            parent[p1] = p2
            rank[p2] += rank[p1]
        else:
            parent[p2] = p1
            rank[p1] += rank[p2]
        return 1
    
    # every time successful union is performed, decrement result by 1
    # res will end with the number of distinct root parents, which is the number of connected components in the graph
    for a, b in edges:
        res -= union(a, b)
    return res

# n = 6
# edges = [[0,1], [1,2], [2,3], [4,5]]
# print(countComponents(n, edges))