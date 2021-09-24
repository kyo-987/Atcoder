
Q=int(input())
q_list=[]
ans_list=[]
in_back=[]
for i in range (Q):
    q=list(map(int, input().split()))
    q_list.append(q)

for q in q_list:
    if q[0]==1:
        in_back.append(q[1])
        in_back.sort()
    elif q[0]==2:
        for i in range(len(in_back)):
            in_back[i]=in_back[i]+q[1]
        
    elif q[0]==3:
        ans_list.append(in_back[0])
        in_back=in_back[1:]
    else:
        print("Error")
for i in ans_list:
    print(i)
