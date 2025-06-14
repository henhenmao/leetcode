
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


n = 6
edges = [[0,1], [1,2], [2,3], [4,5]]

print(countComponents(n, edges))