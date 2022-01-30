Cl=int(input())
L=[]
D=[]
Likei=[]
Dlikei=[]
for i in range(0,Cl):
    L.append(input().split())
    D.append(input().split())

for j in range(0,len(L)):
    for i in range(1,len(L[j])):
        Likei.append(L[j][i])

for j in range(0,len(D)):
    for i in range(1,len(D[j])):
        Dlikei.append(D[j][i])

for j in Dlikei:
    for i in Likei:
        if j == i:
            Likei.remove(j)

Likei=list(set(Likei))
print(len(Likei),end=" ")
for i in Likei:
    print(i,end=" ")