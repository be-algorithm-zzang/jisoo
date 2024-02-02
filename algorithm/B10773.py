import sys
from collections import deque

input=sys.stdin.readline

K=int(input())
graph=[]

for i in range(K):
    num=int(input())
    if num==0:
        graph.pop()
    else:
        graph.append(num)

print(sum(graph))