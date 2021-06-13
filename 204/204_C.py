import sys
input = sys.stdin.readline
import numpy as np
N,M = map(int, input().split())
V_list=[]
for i in range(M):
    Ai,Bi=map(int, input().split())
    V_list.append([Ai,Bi])

t_list=[]
for i in range(0,N):
    t_list.append([i+1])

for i in range(M):
    t_list[V_list[i][0]-1].append(V_list[i][1])

def vi(t_list,V_list):
    frag=1
    t_len=len(t_list)
    while(frag):
        frag=0
        for i in t_list:
            for j in range(1,len(i)):
                new_num=list(set(t_list[i[j]-1])-set(i))
                if len(new_num)>0:
                    frag = 1
                    for k in new_num:
                        i.append(k)

    count=0
    for s in range(len(t_list)):
        count=count+len(t_list[s])
    print(count)
vi(t_list,V_list)
