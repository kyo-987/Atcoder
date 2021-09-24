X=str(input())

x1=int(X[0])
x2=int(X[1])
x3=int(X[2])
x4=int(X[3])

xl=[x1,x2,x3,x4]

pre=x1
flg=1
count=0
for x in xl[1:]:
    count=count+1
    if x1 != x:
        break
    elif count == 3:
        print("Weak")
        flg=0


count=0
if flg ==1:
    for x in xl[1:]:
        count=count+1
        if x==(pre+1)%10:
            pre=x
            if count==3:
                print("Weak")
                flg=0
        else:
            break
if flg==1:
    print("Strong")