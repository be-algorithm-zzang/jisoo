from collections import deque

N=int(input())

graph=[]

for i in range(N):
    graph.append(list(map(int, input().split())))

visited=[[0]*N for _ in range(N)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]



def bfs(x, y):
    size=2
    fish=0
    q=deque()
    q.append([x, y])

    cnt=0

    while q:
        cnt+=1
        if cnt>N*N:break
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if 0<graph[nx][ny]<size:
                    # 물고기가 있는 경우 먹기
                    fish+=1
                    if fish==size:
                        size+=1
                        fish=0
                    visited[nx][ny]=visited[x][y]+graph[nx][ny]
                    graph[nx][ny]=0
                    q.append([nx, ny])
                elif graph[nx][ny]==size or graph[nx][ny]==0:
                    # 지나가기
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx, ny])
    

zero=0
answer=0
for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            zero+=1

if zero==N*N-1:
    answer=0

else:
    for i in range(N):
        for j in range(N):
            if graph[i][j]==9:
                bfs(i, j)

    answer=max(max(visited))

print(answer)
print(visited)