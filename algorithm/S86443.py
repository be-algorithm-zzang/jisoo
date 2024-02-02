import sys

input=sys.stdin.readline

N, M=map(int, input().split())
rules=[]
for i in range(N):
    rules.append(list(map(int, input().split())))

tests=[]
for i in range(M):
    tests.append(list(map(int, input().split())))

i=0
j=0
answer=[]
while True:
    if i>=N or j>=M:break;
    if rules[i][0]<tests[j][0]:
        if tests[j][1]>rules[i][1]:
            answer.append(tests[j][1]-rules[i][1])
            tests[j][0]-=rules[i][0]
        else:
            answer.append(0)
        i+=1
    elif rules[i][0]==tests[j][0]:
        if tests[j][1]>rules[i][1]:
            answer.append(tests[j][1]-rules[i][1])
        else:
            answer.append(0)
        i+=1 
        j+=1
    else:
        if tests[j][1]>rules[i][1]:
            answer.append(tests[j][1]-rules[i][1])
            rules[i][0]-=tests[j][0]
        else:
            answer.append(0)
        j+=1

print(max(answer))
        
        
