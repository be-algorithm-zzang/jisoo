import sys
from collections import deque

input=sys.stdin.readline

n, m=map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    q=deque()
    q.append([x, y])
    graph[x][y]=0

    count=1

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1:
                    count+=1
                    q.append([nx, ny])
                    graph[nx][ny]=0
    return count


drawings=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            d=bfs(i, j)
            drawings.append(d)

print(len(drawings))
maximum=0

for i in range(len(drawings)):
    if drawings[i]>maximum:
        maximum=drawings[i]
print(maximum)