#N,K = map(int, input().split())
N=1
K=2
def sum_m(N,K):
    n=0
    for i in range(1,N+1):
        for j in range(1,K+1):
            n=n+100*i+j
    print(n)
sum_m(N,K)