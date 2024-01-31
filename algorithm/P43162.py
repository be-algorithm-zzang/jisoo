from collections import deque


def solution(n, computers):
    def bfs(i, j):
        q=deque()
        computers[i][j]=0
        computers[i][i]=0
        computers[j][j]=0
        q.append([i, j])

        result=0

        while q:
            x, y=q.popleft()
            for a in range(n):
                if a!=y and computers[y][a]==1:
                    computers[y][a]=0
                    computers[y][y]=0
                    computers[a][a]=0
                    q.append([y, a])

        result+=1

        return result
    
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                answer+=bfs(i, j)
            
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                answer+=1
                
    return answer