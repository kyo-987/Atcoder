import numpy as np

N,M=map(int, input().split())
rode=[]
for i in range(M):
    A,B=map(int, input().split())
    rode.append([A,B])

ans_list=[0 for i in range(N)]
time_map=[]
for i in range(N):
    time_map.append([0 for i in range(N)])

for i in range(M):
    time_map[rode[i][0]-1][rode[i][1]-1]=1
    time_map[rode[i][1]-1][rode[i][0]-1]=1

list_1=time_map[0][1:]
print(list_1)


