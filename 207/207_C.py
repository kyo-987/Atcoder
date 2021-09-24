N=int(input())
in_list=[]
for i in range(N):
    t,l,r = map(int, input().split())
    in_list.append([t,l,r])
in_list2=sorted(in_list, key=lambda x: x[1])   

#print(in_list2)
i=0
ans=0
for i_part in in_list2:
    for j_part in in_list2[i+1:]:
        if i_part[2] == j_part[1]:
            if (i_part[0]%2 != 0) & (j_part[0] < 3):
                ans += 1
        elif i_part[2] > j_part[1]:
            ans += 1
    i += 1
print(ans)
