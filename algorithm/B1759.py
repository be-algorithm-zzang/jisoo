from itertools import combinations

L, C=map(int, input().split())
array=list(map(str, input().split()))

cCl=list(combinations(array, L))
dic=[]

for ccl in cCl:
    c=sorted(ccl)

    word=c[0]
    for i in range(1,L):
        word+=c[i]
    dic.append(word)

dic.sort()
answer=[]

for d in dic:
    mo=0
    ja=0
    for i in range(L):
        if d[i]=="a" or d[i]=="e" or d[i]=="i" or d[i]=="o" or d[i]=="u":
            mo+=1
        else:
            ja+=1
    
    if mo>=1 and ja>=2:
        answer.append(d)
    
for a in answer:
    print(a)