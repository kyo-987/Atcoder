P=int(input())
kai=[]
k=1
for i in range(1,11):
    k=k*i
    kai.append(k)


ans=0
for i in reversed(kai):
    if int(P/i)<=100:
        ans = ans + int(P/i)
        P=P-i*(int(P/i))
    else :
        ans =ans+100
        P=P-100*i
print(ans)