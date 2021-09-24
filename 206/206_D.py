N=int(input())
A = list(map(int,input().split()))

if N%2==0:
    a_list=A[:int(N/2)]
    b_list=A[int(N/2):]

else:
    a_list=A[:int(N/2)]
    b_list=A[int(N/2)+1:]

b_list.reverse()

c_list=[]
for i in range(len(a_list)):
    
    a=a_list[i]
    b=b_list[i]

    if a!=b:
        if ([a,b] not in c_list) & ([b,a] not in c_list):
            c_list.append([a,b])
            print(c_list)


print(len(c_list))
