from queue import PriorityQueue

# OPEN to store the fringes.
# CLOSE to store explored nodes.
OPEN=PriorityQueue()
CLOSE=[]

def is_valid(x1,y1):
    # To check if the new co-ordinates are within boundary of grid. 
    return 0<=x1<4 and 0<=y1<4

def euclidean_distance(x1,x2,y1,y2):
    # Returns euclidian distance as h(x) in algorithm.
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def AStar(layout,goal_i,goal_j):
    c=euclidean_distance(0,goal_i,0,goal_j)
    # OPEN.put((f(x),h(x),Parent co-ordinates,Co-ordinates of current node.))
    OPEN.put((0,c,[0,0],[0,0]))
    # To find the start location.
    for i in range(0,4): 
        for j in range(0,4):
            if layout[i][j]==2:
                a=i
                b=j
                break
    flag=0
    j=0
    # Implements A* algorithm.
    while (not OPEN.empty() and not flag==1):
        b=OPEN.get()
        # Append as it will be explored.
        CLOSE.append((b[2],b[3]))
        prev_val=b[1]
        # Possible neighbours of the current popped out position.
        neighbor=[(b[3][0]-1,b[3][1]),(b[3][0],b[3][1]-1),(b[3][0]+1,b[3][1]),(b[3][0],b[3][1]+1)]
        for i in neighbor:
            if is_valid(i[0],i[1])==True: # Check validity of position.
                if layout[i[0]][i[1]]!=1: # Check if it is not block.
                    ed=euclidean_distance(i[0],goal_i,i[1],goal_j) # Get euclidian distance.
                    if j<1: # For iteration >= 1 we need to add 1 as cost while calculating f_new.
                        f_new=prev_val+1+ed
                    else:  # For iteration < 1 we need to calculate f_new without adding 1. 
                        f_new=prev_val+ed
                    if layout[i[0]][i[1]]==3: # Check if it is goal position.
                        CLOSE.append(([b[3][0],b[3][1]],[i[0],i[1]]))
                        flag=1
                    OPEN.put((f_new,ed,[b[3][0],b[3][1]],[i[0],i[1]]))
        j+=1
    print("The path from (0,0) to (",goal_i,",",goal_j,")","is as follows:")
    k=0
    for i in CLOSE:
        if k<(len(CLOSE)-1):
            print(i[1],"->",end='')
        else:
            print(i[1],end='')
        k+=1

print("--------------- ROBOT NAVIGATION PROBLEM ---------------")


layout=[[2,0,0,1],[1,1,0,0],[0,0,1,0],[0,0,1,3]]



print('Following is the layout of Robot navigation problem:\n',layout)

for i in range (0,4):
    for j in range(0,4):
        if layout[i][j]==3:
            goal_i=i
            goal_j=j
            break;

print("Initial position: ( 0 , 0 )")
print("Goal Position: (",goal_i,",",goal_j,")")

AStar(layout,goal_i,goal_j)
