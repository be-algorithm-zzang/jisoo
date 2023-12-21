# from collections import deque
# from itertools import permutations

# N, M=map(int, input().split())
# graph=[]

# for i in range(N):
#     graph.append(list(map(int, input().split())))

# visited=[[False]*M for _ in range(N)]


# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# def bfs(x, y):
#     q=deque()
#     q.append([x, y])
#     visited[x][y]=True

#     value=0

#     while q:
#         x, y=q.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]

#             if 0<=nx<N and 0<=ny<M:
#                 if graph[nx][ny]==2:
#                     visited[nx][ny]=True
#                     value=0
#                     break
#                 else:
#                     if visited[nx][ny]==False and graph[nx][ny]==0:
#                         visited[nx][ny]=True
#                         value+=1
#                         q.append([nx, ny])

#     return value


# zero=[]

# for i in range(N):
#     for j in range(M):
#         if graph[i][j]==0:
#             zero.append([i, j])


# result=[]
# for p in permutations(zero, 3):
#     newGraph=graph
    
#     for n in p:
#         newGraph[n[0]][n[1]]=1
    
#     part=[]
#     for i in range(N):
#         for j in range(M):
#             if newGraph[i][j]==0 and visited[i][j]==False:
#                 value=bfs(i, j)
#                 part.append(value)
#     # print(p)
#     result.append(sum(part))

# # print(max(result))

from collections import deque
from itertools import combinations

N, M=map(int, input().split())
graph=[]

for i in range(N):
    graph.append(list(map(int, input().split())))

visited=[[False]*M for _ in range(N)]
newGraph=[[0]*M for _ in range(N)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y, newGraph):
    q=deque()
    q.append([x, y])
    visited[x][y]=True

    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny]==False and newGraph[nx][ny]!=1:
                    visited[nx][ny]=True
                    newGraph[nx][ny]=2
                    q.append([nx, ny])

    # print(newGraph)
    cnt=0
    for i in range(N):
        for j in range(M):
            if newGraph[i][j]==0:
                cnt+=1
    # print(cnt)
    # print(newGraph)
    return cnt

zero=[]

for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            zero.append([i, j])


result=[]

for p in list(combinations(zero, 3)):
    for i in range(N):
        for j in range(M):
            newGraph[i][j]=graph[i][j]
            visited[i][j]=False

    for n in p:
        newGraph[n[0]][n[1]]=1
    
    part=[]
    for i in range(N):
        for j in range(M):
            if newGraph[i][j]==2 and visited[i][j]==False:
                value=bfs(i, j,newGraph)
    part.append(value)
    
    cnt=sum(part)

    result.append(cnt)
    
# print(result)
print(max(result))