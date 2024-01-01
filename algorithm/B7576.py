from collections import deque

M, N=map(int, input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int, input().split())))

visited=[[False]*M for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

tomato=0
t=0
day=[]

def bfs(x, y):
    # visited=[[False]*M for _ in range(N)]
    visited[x][y]=True
   
    q=deque()
    q.append([x,y])

    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M: 
                if visited[nx][ny]==False:
                    if graph[nx][ny]==0:
                        graph[nx][ny]=1
                        q.append([nx, ny])
                        t+=1

    day.append(t)
    return t


cnt=0
no_tomato=0
answer=0
day_list=[]

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            cnt+=1
        elif graph[i][j]==-1:
            no_tomato+=1

if cnt==M*N-no_tomato:
    answer=0
else:
    time=0
    while True:
        visited=[[False]*N for _ in range(N)]
        if time==M*N:break
        for i in range(N):
            for j in range(M):
                time+=1
                if graph[i][j]==1 and visited[i][j]==False:
                    tomato+=1
                    bfs(i, j)
                print(graph)

    cnt=0
    no_tomato=0
    yes_tomato=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                cnt+=1
            elif graph[i][j]==-1:
                no_tomato+=1
            elif graph[i][j]==1:
                yes_tomato+=1

    if cnt+yes_tomato!=M*N-no_tomato:
        answer=-1
    else:
        answer=tomato


print(answer)
