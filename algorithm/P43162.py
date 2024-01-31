from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(n, computers):
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                q=deque()
                q.append([i, j])
                computers[i][j]=0
                
                while q:
                    x, y=q.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]

                        if 0<=nx<n and 0<=ny<n:
                            if computers[nx][ny]==1:
                                computers[nx][ny]=0
                                q.append([nx, ny])
                
                answer+=1
                
    print(computers)
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
