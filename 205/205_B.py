N=int(input())
l=input()
l=(l.split())
3
l1=[]
for i in l:
    l1.append(int(i))

new_l=sorted(l1)
k=1
for i in new_l:
    if k==i:
        k=k+1
    else :
        print("No")
        break
if k==len(new_l)+1:
    print("Yes")