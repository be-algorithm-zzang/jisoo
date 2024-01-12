# B7576 토마토 다시풀기
from collections import deque

M, N=map(int, input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int, input().split())))

visited=[[False]*M for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]


q=deque()


def bfs():
    while q:
        x, y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==0:
                    q.append([nx, ny])

                    graph[nx][ny]=graph[x][y]+1


for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            q.append([i, j])

bfs()

yes_tomato=0
answer=0


for i in range(N):
    for j in range(M):
        if graph[i][j]>answer:
            answer=graph[i][j]

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            yes_tomato+=1

if yes_tomato>0:
    answer=0

print(answer-1)