
class nodes:
    def __init__(self,listt,val):
        self.value=val
        self.neighbour=listt

vertices=[]
'''
n=int(input("Enter the number of vertices in graph:\t"))
for i in range(0,n):
    listt=[]
    val=input("Enter the value associated with vertex:\t")
    m=int(input("Enter how many neighbours does the vertex have:\t"))
    for j in range(0,m):
        inp=input("Enter neighbour:\t")
        listt.append(inp)
    c=nodes(listt,val)
    vertices.append(c)
'''
c1=nodes(['B','D'],'A')
vertices.append(c1)
c2=nodes(['A','C'],'B')
vertices.append(c2)
c3=nodes(['D','B'],'C')
vertices.append(c3)
c4=nodes(['C','A'],'D')
vertices.append(c4)
c5=nodes(['B','A'],'E')
vertices.append(c5)

print("Following are entered nodes and their neighbours:\n")
for i in vertices:
    print(i.value,"\t",end='')
    print(i.neighbour)

colors=['Red','Green','Blue','Black']
dictt={}

for i in vertices:
    col_rep=[]
    if not dictt:
        dictt[i.value]=colors[0]
    else:
        for j in i.neighbour:
            if j in dictt:
                col_rep.append(dictt[j])
        for j in colors:
            if j not in col_rep:
                dictt[i.value]=j
                break

print("\nFollowing are the colours associated with the vertices in the graph:")
print(dictt)