N=int(input())
name=[]
for i in range(N):
    S=input()
    name.append(S)

flag=0
for i in range(N):
    if name[i] in name[i+1:]:
        flag=1
        break
if flag==0:
    print("No")

else:
    print("Yes")
