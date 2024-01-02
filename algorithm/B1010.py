from itertools import combinations

T=int(input())

def factorial(n):
    f=1

    for i in range(1,n+1):
        f*=i

    return f

for i in range(T):
    N, M=map(int, input().split())

    answer=factorial(M)//(factorial(N)*(factorial(M-N)))

    print(answer)

