import sys

input=sys.stdin.readline

N=int(input())

# 몫이 짝수 
if (N//3)%2==0:
    # 나머지가 짝수
    if (N%3)%2==0:
        print("CY")
    else:
        print("SK")

else:
    # 나머지가 짝수
    if (N%3)%2==0:
        print("SK")
    else:
        print("CY")

