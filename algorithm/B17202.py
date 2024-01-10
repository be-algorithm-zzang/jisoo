

A=str(input())
B=str(input())

dp=[[0]*16 for _ in range(15)]

for i in range(16):
    if i%2==0:
        dp[0][i]=A[i//2]
    else:
        dp[0][i]=B[i//2]

for i in range(1, 15):
    for j in range(0,15):
        dp[i][j]=str((int(dp[i-1][j])+int(dp[i-1][j+1]))%10)

print(dp[-1][0]+dp[-1][1])