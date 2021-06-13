N= int(input())

d={}
for i in range(N):
    m_name,m_high = map(str,input().split())
    m_high=int(m_high)
    d["m_high"]=m_name

h_list=sorted(d.keys())
n=len(h_list)
print(d[h_list[n-2]])
