A,B,C,D = map(int, input().split())
M=A
R=0
count=0
while(1):
    if C*D <= B:
        print(-1)
        break
    if M<=D*R:
        print(count)
        break
    else :
        M=M+B
        R=R+C
        count=count+1
    