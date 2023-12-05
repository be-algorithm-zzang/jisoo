from collections import deque

R, C=map(int, input().split())
graph=[list(input().strip()) for _ in range(R)]
visited=[[False]*C for _ in range(R)]

# for i in range(R):
#     graph.append(list(str(input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x, y):
    k_count=0
    v_count=0

    visited[x][y]=True 
    queue=deque()
    queue.append([x, y])

    while queue:
        x, y=queue.popleft()
        if graph[x][y]=="v":
            v_count+=1
        if graph[x][y]=="k":
            k_count+=1
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny]!="#" and visited[nx][ny]==False:
                    visited[nx][ny]=True #여기서 visited처리 꼭 해주기!!
                    queue.append([nx, ny])
        
    
    if k_count<=v_count:
        k_count=0
    else:
        v_count=0

    return [k_count, v_count]

answer=[0,0]
for i in range(R):
    for j in range(C):
        if graph[i][j]!="#" and visited[i][j]==False:
            k,v=bfs(i, j)
            answer[0]+=k
            answer[1]+=v


print(answer[0], answer[1])