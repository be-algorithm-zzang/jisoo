import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
graph=[]

for i in range(N):
    graph.append(list(map(int, input().strip())))

visited=[[False]*N for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    q=deque()
    q.append([x,y])
    visited[x][y]=True
    count=1
    break_point=0

    while q:
        x, y=q.popleft()
        break_point+=1
        if break_point>N*N:break;
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]==1 and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    count+=1
                    q.append([nx, ny])

    return count

answer=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and visited[i][j]==False:
            count=bfs(i, j)
            answer.append(count)

answer.sort()
print(len(answer))
for a in answer:
    print(a)

