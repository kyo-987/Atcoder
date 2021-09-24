import numpy as np
N,Q=map(int,input().split())
A = list(map(int,input().split()))
kl=[]
for i in range(Q):
    j = int(input())
    kl.append(j)
#all_list=list(np.arange(1,N+Q+1+max(kl)))
all_list=[]
for i in range(1,N+Q+1+max(kl)):
    all_list.append(i)
for Ai in A:
    all_list.remove(Ai)
for ki in kl:
    print(all_list[ki-1])