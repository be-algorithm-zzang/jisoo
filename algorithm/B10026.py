import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
graph=[]

for _ in range(N):
    graph.append(list(input().strip()))


blind_g=[[0]*N for _ in range(N)]
non_blind_g=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        blind_g[i][j]=graph[i][j]
        non_blind_g[i][j]=graph[i][j]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def blind(x, y, color):
    bq=deque()
    bq.append([x, y])

    blind_g[x][y]="0"
    count=1

    while bq:
        x, y=bq.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if color=="R":
                    if blind_g[nx][ny]=="R" or blind_g[nx][ny]=="G":
                        count+=1
                        blind_g[x][y]="0"
                        bq.append([nx, ny])
                elif color=="B":
                    if blind_g[nx][ny]=="B":
                        count+=1
                        blind_g[x][y]="0"
                        bq.append([nx, ny])
        
    return count

def non_blind(x, y, color):
    q=deque()
    q.append([x, y])
    non_blind_g[x][y]="0"
    count=1

    while q:
        x, y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if non_blind_g[nx][ny]==color:
                    count+=1
                    non_blind_g[x][y]="0"
                    q.append([nx, ny])
        
    return count
        
# 적록색약인 경우
blind_colors=[0,0]
for i in range(N):
    for j in range(N):
        if blind_g[i][j]=="R" or blind_g[i][j]=="G":
            count=blind(i, j, "R")
            if count>1:
                blind_colors[0]+=1
        if blind_g[i][j]=="B":
            count=blind(i, j, "B")
            if count>1:
                blind_colors[1]+=1

# 적록색약 아닌 경우
non_blind_colors=[0,0,0]
for i in range(N):
    for j in range(N):
        if non_blind_g[i][j]=="R":
            n_count=non_blind(i, j, "R")
            if n_count>1:
                non_blind_colors[0]+=1
        elif non_blind_g[i][j]=="B":
            n_count=non_blind(i, j, "B")
            if n_count>1:
                non_blind_colors[2]+=1
        elif non_blind_g[i][j]=="G":
            n_count=non_blind(i, j, "G")
            if n_count>1:
                non_blind_colors[1]+=1


print(sum(non_blind_colors), end=" ")
print(sum(blind_colors))