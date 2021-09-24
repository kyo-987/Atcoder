N = int(input())
ans = []

while N!=1:
    
    if N%2==0:
        ans.append("B")
    else:
        ans.append("A")
        ans.append("B")
    N = N //2
ans.append("A")
print(''.join(ans[::-1]))