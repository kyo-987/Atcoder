import itertools
S,K=input().split()
K=int(K)
all=[]
c = itertools.permutations(S, len(S))
for v in c:
  v1=list(v)
  v2=''.join(v1)
  all.append(v2)
ans=sorted(list(set(all)))
print(ans[K-1])