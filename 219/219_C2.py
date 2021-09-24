X = list(input())
N = int(input())
dic = {}
re_dic={}
for i,j in zip(X,range(1,27,1)):
    dic[i]=j
    re_dic[j]=i

S = []
for i in range(N):
    pre = list(input())
    S.append([dic[i] for i in pre]) 

sorted_S = sorted(S)
for j in sorted_S:
    pre2 = [re_dic[i] for i in j]
    print("".join(pre2))