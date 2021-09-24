N,Q=map(int,input().split())
A = list(map(int,input().split()))
kl=[]
for i in range(Q):
    j = int(input())
    kl.append(j)
for ki in kl:
    re=ki 
    for i in A:
        if i <= re:
            re=re+1
            if i==A[-1]:
                print(re)
        else:
            print(re)
            break

