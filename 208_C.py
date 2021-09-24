N,K = map(int, input().split())

a=list(map(int, input().split()))
b=[]
for i in range(N):
    b.append([i+1,a[i]])
sorted_b=sorted(b, key=lambda x: x[1])  

n=K//N
K2=K%N
for i in range(K2):
    sorted_b[i].append(n+1)
for i in range(K2,N):
    sorted_b[i].append(n)
ans=sorted(sorted_b, key=lambda x: x[0])   
for i in ans:
    print(i[-1])

"""
if K>=N:
    n=K//N
    K2=K%N
    for i in range(K2):
        sorted_b[i].append(n+1)
    for i in range(K2,N):
        sorted_b[i].append(n)
else:
    for i in range(K):
        sorted_b[i].append(1)
    for i in range(K,N):
        sorted_b[i].append(0)
ans=sorted(sorted_b, key=lambda x: x[0])   
for i in ans:
    print(i[-1])
"""