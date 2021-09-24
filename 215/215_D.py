import math
import numpy as np
N,M = map(int, input().split())
A=list(map(int, input().split()))
A_all=1
for i in A:
    A_all=A_all*i
pre_list=[]

for i in range(2,M+1):
    if (A_all % i) != 0:
        pre_list.append(i)

sosuu=[]
for i in pre_list:
    for j in range(2,int(math.sqrt(i)+1)) :
        if i%j==0:
            break
        if j==int(math.sqrt(i)):
            sosuu.append(i) 

all_list=[]
all_list.append(1)
for i in sosuu:
    all_list.append(i)

pre1=sosuu.copy()


    

          


    