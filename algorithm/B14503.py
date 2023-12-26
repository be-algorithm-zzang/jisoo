N, M=map(int, input().split())
r, c, d=map(int, input().split())

graph=[]

for i in range(N):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

cnt=0

while True:
    if r<0 or r>=N or c<0 or c>=M:
        break
    

    if graph[r][c]==0:
        cnt+=1
        graph[r][c]=2
    
    list=[]
    for i in range(4):
        nx=r+dx[i]
        ny=c+dy[i]

        if 0<=nx<N and 0<=ny<M:
            list.append(graph[nx][ny])

    if 0 in list:
        # 반시계 회전
        if d==0:
            d=3
        elif d==1:
            d=0
        elif d==2:
            d=1
        elif d==3:
            d=2
    
        if d==0:
            if 0<=r-1<N and graph[r-1][c]==0:
                r=r-1
        elif d==1:
            if 0<=c+1<M and graph[r][c+1]==0:
                c=c+1
        elif d==2:
            if 0<=r+1<N and graph[r+1][c]==0:
                r=r+1
        elif d==3:
            if 0<=c-1<M and graph[r][c-1]==0:
                c=c-1
    else:
        if d==0:
            r=r+1
        elif d==1:
            c=c-1
        elif d==2:
            r=r-1
        elif d==3:
            c=c+1
    
        if graph[r][c]==1:
            break


print(cnt)
