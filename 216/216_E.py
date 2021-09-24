N,K = map(int, input().split())

A=list(map(int, input().split()))

A=sorted(A)
A=list(reversed(A))

EM=0
j=1
count=0
while(count<K):
    #print(A)
    if(A[0]==0):
        break
    EM=EM+A[0]
    count=count+1
    #print(A[0] == A[j])
    while (count < K ):
        if (A[0]==A[j]):
            EM=EM+A[0]
            A[j]=A[j]-1
            j=j+1
            if j==N:
                break
            count=count+1
        else:
            break
    j=1
    A[0]=A[0]-1
print(EM)
#print(count)


