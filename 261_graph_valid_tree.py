

from typing import List

"""
261. Graph Valid Tree (https://neetcode.io/problems/valid-tree?list=blind75) ()
this was a problem in NeetCode roadmap and is locked behind premium in LeetCode

conditions for a tree in graph theory:
    1. there are n vertices and n-1 edges
    2. all nodes are connected
    3. acyclic
    4. undirected

each pair of nodes in the edges array represents an undirected edge
    in the question we can assume that there will be no duplicate edges in the edges array
    so we can skip condition 2

we need to check for conditions 1, 2, 3
    condition 1:
        just have one line that check for n-1 edges and return False straight up if not fulfilled

    condition 2:
        use a traversal to count each node that can be visited and compare the count with number of nodes n

    condition 3:
        we can find cycles by using a visited array
            during the traversal if you revisited that has been marked as visited then there is a cycle 
            since the edge [0,1] and [1,0] can be considered as a cycle, we just keep track of each node's parent and ignore it

i will use a dfs to traverse the graph


runtime: O(V + E) where V is the number of vertices and E is the number of edges
space: O(V + E) for visited array and adjacency list
"""

def validTree(n: int, edges: List[List[int]]) -> bool:
    # condition 1
    if len(edges) != n-1:
        return False
    
    if len(edges) == 0:
        return True

    # create an adjacency list
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # for node in range(n):
    #     print(f"node {node}: {adj[node]}")
    
    visited = [False] * n
    parent = [-1] * n # parent[i] is the parent of i
    count = 1 # counts number of nodes
    
    # traverse every node in the graph and try to find cycles
    def dfs(curr):
        nonlocal count
        temp = True
        for node in adj[curr]:
            if parent[curr] == node:
                continue
            if visited[node]:
                return False
            
            parent[node] = curr
            visited[node] = True
            count += 1
            temp = temp and dfs(node)
        return temp

    # conditions 2 and 3
    return dfs(edges[0][0]) and count == n


# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# print(validTree(n, edges))