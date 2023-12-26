# from collections import deque

# N=int(input())
# C=int(input())

# visited=[False]*(N+1)

# graph=[]
# graph.append([])

# for i in range(C):
#     graph.append(list(map(int, input().split())))

# def bfs(graph, start, visited):
#     queue = deque([start])

#     visited[start]=True
#     cnt=0

#     while queue:
#         v=queue.popleft()
#         if not 0<=v<C:break;
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True
#                 cnt+=1
    
#     return cnt

# for i in range(C):
#     if graph[]

# answer=bfs(graph, 1, visited)

# print(answer)



# import sys
# from collections import defaultdict, deque

# input = sys.stdin.readline
# num = int(input())  # 컴퓨터의 수
# link = int(input())
# dic = defaultdict(set)

# for i in range(link):
#     a, b = map(int, input().split())
#     dic[a].add(b)
#     dic[b].add(a)

# virus = 0

# visited = [False]*(num+1)


# def bfs(dic, start, visited, virus):
#     queue = deque([start])

#     while queue:
#         j = queue.popleft()
#         for i in dic[j]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#                 virus += 1
#     return virus


# print(bfs(dic, 1, visited, virus)-1)

from collections import deque

N=int(input()) # 컴퓨터 개수
C=int(input()) # 연결선 개수

graph = [[] for i in range(N+1)] # 그래프 초기화
visited=[0]*(N+1) # 방문한 컴퓨터인지 표시

for i in range(C): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향

# print(graph)
visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시
q=deque([1])
cnt=0

while q:
    c=q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            q.append(nx)
            visited[nx]=1
            cnt+=1
            
print(cnt)