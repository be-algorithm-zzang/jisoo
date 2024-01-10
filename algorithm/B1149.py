# N=int(input())

# graph=[]

# for i in range(N):
#     R, G, B=map(int, input().split())
#     graph.append([R , G, B])

# def solution(idx):
#     dp=[0 for _ in range(N+1)]

#     dp[0]=min(graph[idx])

#     idx=-1
#     for i in range(1, N):
#         for k in range(3):
#             if dp[i-1]==graph[i-1][k]:
#                 if idx!=k: #if 2!=0: idx=0
#                     idx=k
#                     break;

#         idx_arr=[]
#         for j in range(3):
#             if j!=idx:
#                 idx_arr.append(j)

#         dp[i]=min(graph[i][idx_arr[0]], graph[i][idx_arr[1]])

  
#     return sum(dp)
# # print(sum(dp))
# # print(dp)

# answer=[]
# for i in range(3):
#     answer.append(solution(i))

# print(answer)
# # print(min(answer))


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