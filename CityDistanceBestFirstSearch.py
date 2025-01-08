from queue import PriorityQueue

OPEN=PriorityQueue()
CLOSE=[]

def BestFSearch(start,destination,nodelist):
    flag=False 
    for i in nodelist:
        if i.name==start:
            bo=i
            break
    CLOSE.append((bo.name,bo.dist))
    for i in nodelist:
        if i.name==destination:
            des_id=i.name
            des_dist=i.dist
            break
    for u in bo.neighbour:
        for ko in nodelist:
            if u==ko.name:
                v=ko.name
                d=ko.dist
                OPEN.put((d,v))
                if ko.name==des_id:
                    flag=True
                    CLOSE.append((des_id,des_dist))
    while ((not OPEN.empty()) and (flag!=True)):
        nextt=OPEN.get()
        for i in nodelist:
            if i.name==nextt[1]:
                bo=i
                break
        CLOSE.append((bo.name,bo.dist))
        for u in bo.neighbour:
            for ko in nodelist:
                if u==ko.name:
                    v=ko.name
                    d=ko.dist
                    if (v,d) not in CLOSE:
                        OPEN.put((d,v))
                    if ko.name==des_id:
                        flag=True
                        CLOSE.append((des_id,des_dist))
    print("\n---------- SOLUTION ----------\nThe path from "+start+" to "+destination+" is as follows:-")
    mn=0
    for k in CLOSE:
        if mn!=(len(CLOSE)-1):
            print(k[0],"-> ",end='')
        else: 
            print(k[0],end='')
        mn+=1

class destinations:
    def __init__(self):
        self.neighbour=[]
    def add_desin(self,name,dist):
        self.name=name
        self.dist=dist
    def add_neighbours(self,name):
        self.neighbour.append(name)

list_nodes=[]
print("--------------- BEST FIRST SEARCH ALGORITHM ---------------\n")
num_destinations=int(input("Please enter how many cities are there on map:\t"))
print("\nWhen you are entering the start city please enter city distance as 0!")
for i in range(0,num_destinations):
    c=destinations()
    jk=input("\nPlease enter name of city:\t")
    dis=int(input("Please enter distance between "+jk+" and your destination: "))
    c.add_desin(jk,dis)
    u=int(input("Enter how many neighbouring cities does the city have:\t"))
    for j in range(0,u):
        cp=input("Input name of city:\t")
        c.add_neighbours(cp)
    list_nodes.append(c)
start=input("\nEnter your start city:\t")
destination=input("Enter your destination city:\t")
BestFSearch(start,destination,list_nodes)
