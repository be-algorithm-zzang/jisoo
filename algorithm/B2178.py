import sys
from collections import deque

input=sys.stdin.readline

N, M=map(int, input().split())
graph=[]

for _ in range(N):
    graph.append(list(map(int, input().strip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    q=deque()
    q.append([x, y])
    c=0

    while q:
        c+=1
        if c>N*M:break # 혹시나 계속 돌 경우를 대비해 break포인트 설정

        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    q.append([nx, ny])

bfs(0,0)
print(graph[-1][-1])