

"""
this problem is actually from USACO 2015 that classmate asked me to do
"""


import sys

sys.stdin = open("bcount.in", "r")
sys.stdout = open("bcount.out", "w")

n, q = [int(i) for i in input().split()]
cows = []
queries = []

for i in range(n):
    cows.append(int(input()))
for i in range(q):
    queries.append([int(i) for i in input().split()])

a = [0] * (n+1)
b = [0] * (n+1)
c = [0] * (n+1)

for i in range(1, n+1):
    if cows[i-1] == 1:
        a[i] = a[i-1] + 1
        b[i] = b[i-1]
        c[i] = c[i-1]
    elif cows[i-1] == 2:
        a[i] = a[i-1]
        b[i] = b[i-1] + 1
        c[i] = c[i-1]
    elif cows[i-1] == 3:
        a[i] = a[i-1]
        b[i] = b[i-1]
        c[i] = c[i-1] + 1

for query in queries:
    l = query[0]
    r = query[1]
    
    acount = a[r] - a[l-1]
    bcount = b[r] - b[l-1]
    ccount = c[r] - c[l-1]

    print(f"{acount} {bcount} {ccount}")


