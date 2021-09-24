N,M=map(int, input().split())
rode=[]
for i in range(M):
    A,B=map(int, input().split())
    rode.append([A-1,B-1])
graph=[]
for i in range(N):
    graph.append([])

for part in rode:
    graph[part[0]].append([part[1],1])
    graph[part[1]].append([part[0],1])

print(graph)