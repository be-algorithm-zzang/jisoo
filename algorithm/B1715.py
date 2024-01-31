import heapq

N=int(input())
cards=[]

for i in range(N):
    cards.append(int(input()))

cards.sort()

if len(cards)==1:
    print(0)

else:
    answer=0
    while len(cards)>1:
        one=heapq.heappop(cards)
        two=heapq.heappop(cards)
        com=one+two
        answer+=com
        heapq.heappush(cards, com)
    print(answer)