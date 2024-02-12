import sys
from collections import deque

input=sys.stdin.readline

N, K=map(int, input().split())

q=deque()
q.append(N)

MAX=100000
g=[0] * (MAX + 1)

while q:
    x=q.popleft()
    if x==K:
        print(g[x])
        break;
    
    dx=[-1,1,x]

    for i in range(3):
        nx=x+dx[i]

        if 0<=nx<=MAX and not g[nx]:
            g[nx]=g[x]+1
            q.append(nx)
