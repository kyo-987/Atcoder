N=input()

X,Y=N.split(".")
X=int(X)
Y=int(Y)
if 0<=Y | Y<=2:
    print(str(X)+"-")
elif 3<=Y | Y<=6:
    print(X)
else:
    print(str(X)+"+")