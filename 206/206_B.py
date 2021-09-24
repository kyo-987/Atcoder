def tsum(i):
    if i==1:
        return 1
    else:
        s=(1+i)*i/2
    return s
N=int(input())
i=1
while(1):
    if tsum(i) < N:
        i=i+1
    else:
        print(i)
        break
