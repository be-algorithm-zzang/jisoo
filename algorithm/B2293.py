import sys

input=sys.stdin.readline

n, k=map(int, input().split())
coins=[]

for i in range(n):
    coins.append(int(input()))

dp=[0 for _ in range(k+1)]
dp[0]=1

coins.sort()

for i in coins:
    for j in range(i, k+1):
        dp[j]+=dp[j-i]

print(dp[-1])