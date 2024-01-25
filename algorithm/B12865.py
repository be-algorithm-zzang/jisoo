# from itertools import combinations

# N, K=map(int, input().split())
# bags=[]
# for i in range(N):
#     W, V=map(int, input().split())
#     bags.append([W,V])

# idx=[]
# for i in range(N):
#     idx.append(i)

# values=[]
# for i in range(N):
#     # 4, 3, 2, 1 전부 탐색
#     nCi=list(combinations(idx,i))

#     weight=0
#     value=0

#     for j in nCi:
#         # 무게
#         weight+=bags[j][0]
#         # 가치
#         if weight>=K:
#             value+=bags[j][1]
    
#     values.append(value)

# print(max(values))

N, K=map(int, input().split())
bags=[[0,0]]
for i in range(N):
    W, V=map(int, input().split())
    bags.append([W,V])
bags.sort()

dp=[[0,0] for _ in range(N+1)]

for i in range(1,N+1):
    if dp[i-1][0]+bags[i][0]<=K:
        dp[i][0]=dp[i-1][0]+bags[i][0]
        dp[i][1]=dp[i-1][1]+bags[i][1]

    else:
        dp[i][1]=max(dp[i-1][1], bags[i][1])
        if dp[i][1]==dp[i-1][1]:
            dp[i][0]=dp[i-1][0]
        else:
            dp[i][0]=bags[i][0]

print(dp)
print(dp[-1][1])
