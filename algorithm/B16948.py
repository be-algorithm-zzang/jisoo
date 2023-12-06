from collections import deque

N=int(input())
r1, c1, r2, c2=map(int, input().split())
visited=[[-1]*N for _ in range(N)]

dx=[-2,-2,0,0, 2, 2]
dy=[-1,1,-2,2,-1,1]

def bfs(x, y):
    visited[x][y]=0;
    queue=deque()
    queue.append([x, y])

    move=0
    cycle=0

    while queue:
        x, y=queue.popleft()
        move+=1
        cycle+=1
        if x==r2 and y==c2:
            break;
        if cycle>=N**2:
            move=-1
            break;

        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==-1:
                    queue.append([nx,ny])
                    visited[nx][ny]=visited[x][y]+1


bfs(r1,c1)
print(visited[r2][c2])
