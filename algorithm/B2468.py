import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

graph=[]

for i in range(N):
    graph.append(list(map(int, input().split())))

maximum=0

for i in range(N):
    for j in range(N):
        if graph[i][j]>maximum:
            maximum=graph[i][j]


# 1이면 살아남고, 0이면 물에 잠긴다
# for i in range(m):
#     for j in range(m):
#         if graph[i][j]>=N:
#             graph[i][j]=1
#         else:
#             graph[i][j]=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y, n, visited):
    q=deque()

    graph[x][y]=0
    visited[x][y]=True
    q.append([x, y])

    count=0
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]>n and visited[nx][ny]==False:
                    q.append([nx, ny])
                    count+=1
    return count
    

answer=[]

for m in range(maximum):
    safe=[]
    visited=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 안전영역인 경우
            if graph[i][j]>=m and visited[i][j]==False:
                safe.append(bfs(i, j, m, visited))
    answer.append(len(safe))

print(len(answer))