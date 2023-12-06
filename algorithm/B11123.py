from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    visited[x][y]=True
    queue=deque()
    queue.append([x,y])
    sheep=1
    cycle=0

    while queue:
        x, y=queue.popleft()
        cycle+=1
        if cycle>=H*W:break
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<H and 0<=ny<W:
                if visited[nx][ny]==False and graph[nx][ny]!=".":
                    visited[nx][ny]=True
                    sheep+=1
                    queue.append([nx, ny])
    # print(sheep)
    return sheep


T=int(input())


answer=[]
for t in range(T):
    result=[]
    H, W=map(int, input().split())
    graph=[list(input().strip()) for _ in range(H)]
    visited=[[False]*W for _ in range(H)]
    
    for i in range(H):
        for j in range(W):
            if visited[i][j]==False and graph[i][j]!=".":
                result.append(bfs(i,j))

    answer.append(len(result))

for a in answer:
    print(a)