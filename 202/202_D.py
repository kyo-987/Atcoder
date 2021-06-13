a,b,k = map(int, input().split())
count=k
ac=a
bc=b
re=""
import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(a+b):
    print(bc)
    if (ac>0) & (bc>0):
        c=comb(ac-1+bc,bc)
        if c < count:
            re = re + "b"
            bc=bc-1
            count=count-c
        else :
            re = re + "a" 
            ac=ac-1
    else:
        if ac == 0:
            re = re + "b"
        if bc==0:
            re = re +"a"
print(re)


