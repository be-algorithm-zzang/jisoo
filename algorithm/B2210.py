
graph=[]

for i in range(5):
    graph.append(list(map(int, input().split())))

complete=[]

def dfs(x, y, number):
    if len(number)==6:
        if number not in complete:
            complete.append(number)
        return;
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
    
        if nx>=0 and nx<5 and ny>=0 and ny<5:
            dfs(nx, ny, number+str(graph[nx][ny]))

for i in range(5):
    for j in range(5):
        dfs(i, j, str(graph[i][j]))

print(len(complete))