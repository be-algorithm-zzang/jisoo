# one=str(input())
# two=str(input())

# N=len(one)
# M=len(two)

# graph=[[0]*(N+1) for _ in range(M+1)]

# for i in range(1, N+1):
#     for j in range(1, M+1):
#         if two[i-1]==one[j-1]:
#             graph[i][j]=max(graph[i-1][j], graph[i][j-1])+1
#         else:
#             graph[i][j]=max(graph[i-1][j], graph[i][j-1])

# print(graph[-1][-1])

import sys

read = sys.stdin.readline

one, two = read().strip(), read().strip()
N, M = len(one), len(two)
graph = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if one[i-1] == two[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])
print(graph[-1][-1])