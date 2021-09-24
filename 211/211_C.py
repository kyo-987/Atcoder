S=list(input())
sd={"c":[],"h":[],"o":[],"k":[],"u":[],"d":[],"a":[],"i":[]}
sd2={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
l=["c","h","o","k","u","d","a","i"]
lr=reversed(l)
k=0
for i in S:
    if i in l:
        sd[i].append(k)
    k=k+1

count=0
for j in lr:
    if j=="i":
        for c in sd[j]:
            sd2[1].append(1)
        count = count+1
    else:    
        for n1 in sd[lr[count]]:
            sd2[count+1].append(0)
            k=0
            for n2 in sd[lr[count-1]]:
                if n1<n2:
                    sd2[count+1][k]=sd2[count+1][k]

             






        
