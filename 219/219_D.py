import itertools
import sys
N=int(input())
X,Y = map(int, input().split())
lb=[]
for i in range(N):
    A,B= map(int, input().split())
    lb.append([A,B])
for i in range (1,N+1):
    all_list=list(itertools.combinations(lb,i ))
    #print(all_list)
    
    for j in all_list:
        j=list(j)
        ca=0
        cb=0
        for k in j:
            ca=ca+k[0]
            cb=cb+k[1]
        if X<=ca and Y<=cb:
            print(i)
            sys.exit()
    if i==N:
        print(-1)




