N=int(input())
A = list(map(int,input().split()))

pl=list(set(A))
n=len(pl)
print(n*(n-1)/2)