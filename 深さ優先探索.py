V,E = map(int, input().split())
graph=[]
M=[]
for i in range(E):
    inE=list(map(int, input().split()))
    M.append(inE)

for i in range(V):
    graph.append([])

for part in M:
    graph[part[0]].append(part[1])
    graph[part[1]].append(part[0])

print(graph)

seen=[False for i in range(V)]
def dfs(v):
    if not seen[v]:
        seen[v]=True
        for v_next in graph[v]:
            dfs(v_next)

s=3
t=7

dfs(s)
print(seen)
if seen[t]:
    print("can")
else :
    print("can not")


