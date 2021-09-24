import collections
N = int(input())
A = list(map(int, input().split()))
c = collections.Counter(A)
d = c.most_common()
print(c)
print(d)

sum_l = [0] * len(d)
counter = [0] * len(d)
for i in reversed(range(len(d))):
    if i == len(d)-1:
        counter[i] = d[i][1]
    else:
        counter[i] = d[i][1] + counter[i+1]
for i in reversed(range(len(d))):
    if i == len(d)-1:
        sum_l[i] = 0
    else:
        sum_l[i] = d[i][1] * counter[i+1]
print(counter)
print(sum_l)
print(sum(sum_l))