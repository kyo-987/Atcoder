N=int(input())
S=str(input())

for i in range(N):
    if int(S[i])==1:
        if i%2==0:
            print("Takahashi")
            break
        else:
            print("Aoki")
            break