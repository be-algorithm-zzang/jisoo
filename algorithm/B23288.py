from collections import deque

N, M, K=map(int, input().split())
graph=[]

for i in range(N):
    graph.append(input().split( ))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
dice=[[0,2,0],[4,1,3][0,5,0][0,6,0]]
cnt=0

# z는 방향 1동 2서 3남 4북
def bfs(x, y,z):
    visited=[[False]*M for _ in range(N)]
    visited[x][y]=True
    queue=deque()
    queue.append([x,y,z])
    cnt+=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<N and 0<=ny<M:
            if visited[nx][ny]==False:
                if cnt==K:
                    B=graph[nx][ny]
                    visited[nx][ny]=True;
                    queue.append([x,y,z])

    return K*B

bfs(1,1,1)