import sys

input = sys.stdin.readline

N, K=map(int, input().split())
S=list(map(int, input().split()))
array=[]

for i in range(K):
    A, B=map(int, input().split())
    array.append([A,B])
    
for i in range(K):
    score_sum=0
    for j in range(array[i][0]-1,array[i][1]):
        score_sum+=S[j]
    average=score_sum/(array[i][1]-array[i][0]+1)
    round_average=round(average, 2)
    format_score=format(round_average, '.2f')
    print(format_score)
