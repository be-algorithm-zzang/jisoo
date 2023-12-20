from collections import deque


def solution(numbers, target):
    answer = 0

    q=deque()
    q.append((numbers[0],0))
    q.append((-numbers[0],0))
    
    while q:
        n, idx=q.popleft()
        
        if idx==len(numbers)-1:
            if n==target:
                answer+=1
                continue
        if idx+1<len(numbers):
            q.append((n+numbers[idx+1], idx+1))
            q.append((n-numbers[idx+1], idx+1))
    
    return answer

print(solution([4, 1, 2, 1], 4))