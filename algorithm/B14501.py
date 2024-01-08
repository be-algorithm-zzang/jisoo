

N=int(input())
graph=[]

dp=[0 for i in range(N+1)]

for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N-1, -1, -1):
    if i +graph[i][0]>N:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1], graph[i][1]+dp[i+graph[i][0]])

print(dp[0])