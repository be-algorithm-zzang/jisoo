from collections import deque

M, N, H=map(int, input().split())

graph=[]

for h in range(H):
    g=[]
    for i in range(N):
        g.append(list(map(int, input().split())))
    
    graph.append(g)

q=deque()

dh=[-1,1,0,0,0,0]
dx=[0,0,-1,1,0,0]
dy=[0,0,0,0,-1,1]

# 탐색 함수
def bfs():
    while q:
        h, x, y=q.popleft()
        
        for n in range(6):
            nh=h+dh[n]
            nx=x+dx[n]
            ny=y+dy[n]

            if 0<=nh<H and 0<=nx<N and 0<=ny<M:
                if graph[nh][nx][ny]==0:
                    graph[nh][nx][ny]=graph[h][x][y]+1
                    q.append([nh, nx, ny])



# 이미 모두 익어있는 경우
not_ready_tomato=0

for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j]==0:
                not_ready_tomato+=1

if not_ready_tomato==0:
    answer=0

# 안 익은 게 있는 경우
else:
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j]==1:
                    q.append([h, i, j])
    
    bfs()

    not_tomato=0

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j]==0:
                    not_tomato+=1
    
    if not_tomato>0:
        answer=-1
    else:
        min_day=0
        for h in range(H):
            for i in range(N):
                for j in range(M):
                    if graph[h][i][j]>min_day:
                        min_day= graph[h][i][j]
        answer=min_day-1

print(answer)

