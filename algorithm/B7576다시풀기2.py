import sys
from collections import deque

input=sys.stdin.readline

M, N=map(int, input().split())

graph=[]

for _ in range(N):
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
                if graph[nx][ny]==0 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    graph[nx][ny]=graph[x][y]+1
                    q.append([nx, ny])
        
# 처음부터 다 익어있는 지 확인
# 모든 토마토가 익어있으면 안 익은 토마토가 0이다.
first_zero_tomato=0

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            first_zero_tomato+=1

answer=0
# (1) 처음부터 다 익은 경우
if first_zero_tomato==0:
    answer=0
else:
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and visited[i][j]==False:
                # bfs(i, j)
                
                # 1이 있는 곳 동시 시작되어야하므로, 바로 append해주기!
                q.append([i, j])
                graph[i][j]=1
                visited[i][j]=True
    # 시작점이 다 추가된 후에 bfs 돌리면 1이 있는 모든 곳에서 시작됨.
    bfs()
               
    # 순회를 돌고 난 후에도 안 익은 토마토가 있는지 확인
    # 안 익은 토마토가 있으면 토마토가 모두 익지 못하는 상황 
    after_zero_tomato=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                after_zero_tomato+=1
    # (2) 토마토가 다 익지는 못하는 경우
    if after_zero_tomato>0:
        answer=-1
    # (3) 토마토가 다 익는 경우
    else:
        days=0

        for i in range(N):
            for j in range(M):
                if graph[i][j]>days:
                    days=graph[i][j]
        answer=days-1

print(answer)
