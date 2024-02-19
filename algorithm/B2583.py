import sys
from collections import deque

input=sys.stdin.readline

M, N, K=map(int, input().split())
graph=[[0]*M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2=map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j]=1


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    q=deque()
    q.append([x, y])
    graph[x][y]=1

    count=1

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==0:
                    q.append([nx, ny])
                    graph[nx][ny]=1
                    count+=1

    return count


answer=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            answer.append(bfs(i, j))
answer.sort()

print(len(answer))
for a in answer:
    print(a, end=" ")
    
print("\n")