import sys

input=sys.stdin.readline

N=int(input())

origin=N
cnt=0

while True:
    first=N%10
    second=N//10 + first

    N=first*10+second%10

    cnt+=1

    if N==origin:break;

print(cnt)