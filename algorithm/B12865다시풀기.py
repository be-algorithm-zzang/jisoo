
N, K=map(int, input().split())
bags=[[0,0]]
for i in range(N):
    W, V=map(int, input().split())
    bags.append([W,V])

chart = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, K + 1):
        w=bags[i][0]
        v=bags[i][1]

        if j<w:
            chart[i][j]=chart[i-1][j]
        else:
            # j-w는 K-W라고 생각하면 쉽다! -> 최대가 K이기 때문에 K-W가 되면 무조건 최대 무게를 넘지 않게 된다.
            chart[i][j]=max(chart[i-1][j], v+chart[i-1][j-w])

print(chart[N][K])
