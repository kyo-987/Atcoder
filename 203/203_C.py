N,K = map(int, input().split())

f_list=[]
d={}
for i in range(N):
    A,B = map(int, input().split())
    d[A]=B
print(d)
print(d.keys())

def trip(d,K):
    town=0
    while(K!=0):
        K=K-1
        town=town+1
        if town == pow(10,100)-1:
            break
        if town in(d.keys()):
            K=K+d[town]
        if town>max(d.keys()):
            town=town + K
            break
    print(town)   
trip(d,K)     
