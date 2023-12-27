from collections import deque

N=int(input())

graph=[list(input().strip()) for _ in range(N)]

visited=[[False]*N for _ in range(N)]

house=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    q=deque()
    q.append([x, y])
    visited[x][y]=True

    house=1

    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny]=="1" and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    house+=1
                    q.append([nx, ny])

    return house

for i in range(N):
    for j in range(N):
        if graph[i][j]=="1" and visited[i][j]==False:
            house.append(bfs(i,j))

print(len(house))
house.sort()

for i in range(len(house)):
    print(house[i])
