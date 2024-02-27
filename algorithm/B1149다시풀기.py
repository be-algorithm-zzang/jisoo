N=int(input())

graph=[]

for i in range(N):
    R, G, B=map(int, input().split())
    graph.append([R , G, B])

for i in range(1, N):
    graph[i][0]+=min(graph[i-1][1], graph[i-1][2])
    graph[i][1]+=min(graph[i-1][0], graph[i-1][2])
    graph[i][2]+=min(graph[i-1][0], graph[i-1][1])

print(min(graph[-1]))