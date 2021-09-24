X=input()
N=input()
S=[]
for i in range(N):
    Si=input()
    S.append(Si)
ans=[]
def add(ans,S,X):
    for i in X:
        pre=[]
        for j in S:
            i=0
            if j[0]==i:
                pre.append(j)
        if len(pre)==1:
            ans.append(pre[0])
        else:
            add(pre,X)
        

X
