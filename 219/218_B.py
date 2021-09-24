S1=input()
S2=input()
S3=input()
T=list(input())
ans=""

for j in T:
    i=int(j)
    if i==1:
        ans=ans+S1
    elif i==2:
        ans=ans+S2
    else:
        ans=ans+S3
print(ans)