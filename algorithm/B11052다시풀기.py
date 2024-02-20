import sys

input=sys.stdin.readline

N=int(input())

graph=[0]
list=list(map(int, input().split()))

for l in list:
    graph.append(l)

dp=[0]*(N+1)
dp[1]=graph[1]

for i in range(1, N+1):
    flag=[graph[i]]
    for j in range(2, i):
        flag.append(dp[j]+graph[i-j])
    
    dp[i]=max(flag)

print(dp[-1])