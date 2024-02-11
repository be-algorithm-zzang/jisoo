import sys
from collections import deque

input=sys.stdin.readline

q=deque()
jj=deque()

R, C=map(int, input().split())
graph=[]

for _ in range(R):
    graph.append(list(map(str, input().strip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

fire_visited=[[0]*C for _ in range(R)]
j_visited=[[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if graph[i][j]=="F":
            q.append([i, j])
            fire_visited[i][j]=1
        elif graph[i][j]=="J":
            jj.append([i, j])
            j_visited[i][j]=1

def fire():
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if graph[nx][ny] == "#" or fire_visited[nx][ny]:
                continue
            fire_visited[nx][ny] = fire_visited[x][y] + 1
            q.append((nx, ny))
            # if 0<=nx<R and 0<=ny<C:
            #     if graph[nx][ny]!="#" and fire_visited[nx][ny]==0:
            #         q.append([nx, ny])
            #         fire_visited[nx][ny]=fire_visited[nx][ny]+1
                    

def jihoon():
    while jj:
        x, y=jj.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # if 0<=nx<R and 0<=ny<C:
            #     if not j_visited[nx][ny] and graph[nx][ny]!="#" and fire_visited[nx][ny] and j_visited[nx][ny]+1>=fire_visited[nx][ny]:
            #     # if graph[nx][ny]!="." and fire_visited[nx][ny]==0 and j_visited[nx][ny]==0:
            #         j_visited[nx][ny]=j_visited[x][y]+1
            #         jj.append([nx, ny])
            # else:
            #     print(j_visited[x][y])
            #     return
            if not (0 <= nx < R and 0 <= ny < C):
                print(j_visited[x][y])
                return
            if j_visited[nx][ny] or graph[nx][ny] == "#":
                continue
            if fire_visited[nx][ny] and j_visited[x][y] + 1 >= fire_visited[nx][ny]:
                continue
            j_visited[nx][ny] = j_visited[x][y] + 1
            jj.append((nx, ny))
    print("IMPOSSIBLE")
    return


fire()
jihoon()