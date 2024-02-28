import sys

input=sys.stdin.readline

n=int(input())

dp=[0]*(n+1)
dp[0]=0
dp[1]=1
dp[2]=2

for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%10007

# 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지
print(dp[n])

