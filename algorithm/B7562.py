import sys
from collections import deque

input=sys.stdin.readline

T=int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(x, y):
    q=deque()
    q.append([x, y])
    graph[x][y]=1
    cnt=0

    while q:
        cnt+=1
        if cnt>I*I:break

        x, y=q.popleft()
        if x == end_x and y == end_y:
            return graph[x][y] -1 
        
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<I and 0<=ny<I and graph[nx][ny]==0:
                graph[nx][ny]=graph[x][y]+1
                q.append([nx, ny])

for _ in range(T):
    I=int(input())

    start_x, start_y=map(int, input().split())
    end_x, end_y=map(int, input().split())
    
    # if start_x==end_x and start_y==start_y:
    #     print(0)

    # else:
    #     graph=[[0]*I for _ in range(I)]
    #     bfs(start_x, start_y)
    #     print(graph[end_x][end_y])
    graph=[[0]*I for _ in range(I)]
    
    print(bfs(start_x, start_y))
