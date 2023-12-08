from collections import deque

N, M=map(int, input().split())
graph=[]

for i in range(N):
    graph.append(input().split( ))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    graph[x][y]="1"
    queue=deque()
    queue.append([x, y])
    cycle=0

    while queue:
        x, y=queue.popleft()
        cycle+=1

        if cycle>N*M:break

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if ny==M:
                ny=0
            if ny==-1:
                ny=M-1
            if nx==N:
                nx=0
            if nx==-1:
                nx=N-1

            if graph[nx][ny]=="0":
                graph[nx][ny]="1"
                queue.append([nx, ny])

answer=0
for i in range(N):
    for j in range(M):
        if graph[i][j]=="0":
            bfs(i, j)
            answer+=1

print(answer)