N=int(input())
A=input().split()

A_sum=0
for i in A:

    if int(i) > 10:
        A_sum = A_sum + int(i) - 10

print(A_sum)