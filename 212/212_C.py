N,M = map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()
B.sort()
i=0
j=0
min_ab=abs(A[0]-B[0])
while(i!=len(A))&(j!=len(B)):
    min_ab=min(abs(A[i]-B[j]),min_ab)

    if A[i]==B[j]:
        break
    elif A[i]>B[j]:
        j=j+1
    else:
        i=i+1
print(min_ab)