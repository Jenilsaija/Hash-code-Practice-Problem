ui = open("a_an_example.txt")
temp=ui.readlines()
L=[]
D=[]
Like=[]
Dlike=[]
for i in range(1,len(temp)):
    if i%2!=0:
        L.append(temp[i].split())
    else:
        D.append(temp[i].split())

for i in range(0,len(L)):
    for j in range(1,int(L[i][0])+1):
        Like.append(L[i][j])

for i in range(0,len(D)):
    for j in range(1,int(D[i][0])+1):
        Dlike.append(D[i][j])

for j in Dlike:
    for i in Like:
        if j == i:
            Like.remove(j)

Like=list(set(Like))
print(len(Like),end=" ")
for i in Like:
    print(i,end=" ")