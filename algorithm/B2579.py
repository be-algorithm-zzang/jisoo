N=int(input())
array = [0]*301
for i in range(N):
    array[i]=int(input())

dp = [0]*301

# array=[int(input()) for _ in range(N)]
# dp=[0 for _ in range(2*N)]

dp[0]=array[0]
dp[1]=array[0]+array[1]
dp[2]=max(array[0]+array[2], array[1]+array[2])

for i in range(3,N):
    dp[i]=max(array[i]+array[i-1]+dp[i-3], array[i]+dp[i-2])

print(dp[N-1])

# array.reverse()
# dp[0]=array[0]

# i=0
# cnt=0
# while True:
#     if i+2<len(array):
#         if(array[i+1]>=array[i+2]):
#             dp[i+1]=array[i+1]
#             if i+1==len(array)-3 or  i+1==len(array)-2:
#                 cnt+=1
#             dp[i+3]=array[i+3]
#             i+=3
#             # i+=2
        
#         else:
#             dp[i+2]=array[i+2]
#             if i+1==len(array)-3 or  i+1==len(array)-2:
#                 cnt+=1
#             i+=2
#     else:break

# # print(cnt)
# if cnt!=2:
#     dp[len(array)-1]=array[-1]

# answer=0
# for d in dp:
#     answer+=d
# # print(dp)
# # print(array)
# print(answer)