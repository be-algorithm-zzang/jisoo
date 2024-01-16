N=int(input())
pack=list(map(int, input().split()))
p=[0]
p+=pack

dp=[0 for _ in range(N+1)]

dp[1]=p[1]

for i in range(2, N+1):
    flag=[]
    for j in range(1,i):
        flag.append(dp[j]+p[i-j])
    
    flag.append(p[i])
    dp[i]=max(flag)

print(max(dp))
