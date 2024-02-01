import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
maps=[]

for i in range(N):
    maps.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    
    while q:
        x, y=q.popleft();
        
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny]==1:
                    q.append([nx, ny])
                    maps[nx][ny]=maps[x][y]+1
                
                
answer = 0


bfs(0,0)
if maps[-1][-1]==1:
    answer=-1
else:
    answer=maps[-1][-1]


print(answer)