from queue import PriorityQueue

def Astar(start,destination,listnodes):
    OPEN=PriorityQueue()
    CLOSE=[]
    flag=False
    flag2=0
    OPENN=[]

    for i in listnodes:
        if start==i.name:
            contains_start=i
            op=i.dist
            break
    
    neigh_names=[]
    
    for neigh in contains_start.neighbour:
        neigh_names.append(neigh)
    
    for hsld in listnodes:
        #clac=0
        for i in neigh_names:
            if i[0]==hsld.name:
                calc=i[1]+hsld.dist
                OPEN.put((calc,i[0]))

    CLOSE.append((start,op))
    
    Travel=0
    
    while ((not OPEN.empty()) and (flag!=True)):
        nextt=OPEN.get()
        CLOSE.append((nextt[1],nextt[0]))
        for i in listnodes:
            if nextt[1]==i.name:
                contains_city=i
                break;
        neigh_names=[]
        for neigh in contains_city.neighbour:
            neigh_names.append(neigh)

        for hsld in listnodes:
            for i in neigh_names:
                calc=0
                flag2=0
                flag3=0
                if i[0]==hsld.name:
                    calc=hsld.dist+Travel
                    Travel=calc
                    for h in CLOSE:
                        if h[0]==i[0]:
                            flag3=1
                    for t in OPENN:
                        if t[1]==i[0]:
                            flag2=1
                            break
                    if flag2==0 and flag3==0:
                        OPEN.put((calc,i[0]))
                    OPENN.append((calc,i[0]))
                    if hsld.name==destination:
                        flag=True
                        CLOSE.append((hsld.name,calc))
    
    print("The path from "+start+" to "+destination+" is as follows:-")
    
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
    def add_neighbours(self,name,distance):
        self.neighbour.append((name,distance))

list_nodes=[]
print("--------------- A* ALGORITHM ---------------\n")

print("\n*************** INPUT YOUR GRAPH/DATA ***************\n")

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
        disttt=int(input("Enter distance between "+jk+" and "+cp+":\t"))
        c.add_neighbours(cp,disttt)
    list_nodes.append(c)

print("\n*************** ENTER START AND DESTINATION ***************\n")
start=str.upper(input("\nEnter your start city:\t"))
destination=str.upper(input("Enter your destination city:\t"))

print("\n*************** OUTPUT ***************")
Astar(start,destination,list_nodes)