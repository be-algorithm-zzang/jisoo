from collections import deque

N, M=map(int, input().split())
graph=[]

for i in range(N):
    graph.append(list(map(int,input().split())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]
cheese=[]


def bfs():
    visited=[[False]*N for _ in range(N)]
    value=0
    queue=deque()
    queue.append([0, 0])
    visited[0][0]=True

    while queue:
        x, y=queue.popleft()
       
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                if graph[nx][ny]=="1":
                    visited[nx][ny]==True
                    graph[x][y]="0"
                    value+=1
                if graph[nx][ny]=="0":
                    visited[nx][ny]==True
                    queue.append([nx, ny]) 
    cheese.append(value)
    return value


time=0
while True:
    visited=[[False]*N for _ in range(N)]
    time+=1
    value=bfs()
    if value==0:
        break

            

print(time-1)
print(cheese[-2])