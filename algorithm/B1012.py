from collections import deque

T=int(input())


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    q=deque()
    visitied[x][y]=True
    q.append([x,y])

    count=0

    while q:
        x, y=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny]==1 and visitied[nx][ny]==False:
                    visitied[nx][ny]=True
                    count+=1
                    q.append([nx, ny])
    
    return count


for _ in range(T):
    M, N, K=map(int, input().split())

    arr=[]

    for i in range(K):
        x,y=map(int, input().split())
        arr.append([x,y])

    graph=[[0]*M for _ in range(N)]
    visitied=[[False]*M for _ in range(N)]


    for i in range(K):
        graph[arr[i][1]][arr[i][0]]=1

    answer=[]
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 and visitied[i][j]==False:
                answer.append(bfs(i, j))
    
    print(len(answer))