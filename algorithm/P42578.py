from itertools import combinations


def solution(clothes):
    answer = 0
    dic={}
    
    for i in range(len(clothes)):
        if clothes[i][1] in dic.keys():
            dic[clothes[i][1]]+=1
        else:
            dic[clothes[i][1]]=1
    
    counts=dic.values()
    
    
    for i in range(1,len(counts)+1):
        nCi=list(combinations(counts, i))
        
        for n in nCi:
            value=1
            for j in range(len(n)):
                value=value*n[j]
            answer+=value
            
    
    return answer