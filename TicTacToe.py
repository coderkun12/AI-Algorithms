# Tic Tac Toe using Magic Square Method.
import MagicSq as ms 
import numpy as np
import random

def print_board(ar):
    i=0
    while i < 3:
        j=0
        while j<3:
            print("| ",end="")
            if ar[i,j]==-1:
                print(" ",end="")
            elif ar[i,j]==0:
                print("O",end="")
            elif ar[i,j]==1:
                print("X",end="")
            j+=1
        print(" | ")
        i+=1

def get_go(t,magic,move):
    i=1
    p=q=0
    while i<4:
        j=1
        while j<4:
            if magic[i,j]==t:
                p=i
                q=j
            j+=1
        i+=1
    if (move[p-1,q-1]==1) or (move[p-1,q-1]==0):
        return 0
    else:
        return 1

def verification(move,magic,n):
    i=0
    arr=np.zeros(10)
    mag=np.zeros(10)
    k=0
    while i <3:
        j=0
        while j<3:
            if move[i,j]==n:
                arr[k]=i
                k+=1
                arr[k]=j
                k+=1
            j+=1
        i+=1
    if k<=4:
        j=arr[0]
        i=arr[1]
        mag[0]=magic[int(j+1),int(i+1)]
        j=arr[2]
        i=arr[3]
        mag[1]=magic[int(j+1),int(i+1)]
        tryy=15-(mag[0]+mag[1])
        if (tryy>0 and tryy<=9):
            return tryy
    else:
        a=0
        b=0
        while a<k:
            i=arr[a]
            j=arr[a+1]
            mag[b]=magic[int(j+1),int(i+1)]
            b+=1
            a+=2
        i=0
        while i<b:
            j=0
            while j<b:
                tryy=15-(mag[i]+mag[j])
                if (tryy>0 and tryy<=9):
                    op=get_go(tryy,magic,move)
                    if op==1:
                        return tryy
                j+=1
            i+=1
        i=0
    return 0

def tic_tac_toe(magic):
    move=np.zeros([3,3])
    move[:,:]=-1
    flag=0
    print("When asked to play the user should enter the number associated with the space on the game board. Please refer the numbers on board below:")
    k=1
    i=0
    refe=np.zeros([3,3])
    while i<3:
        j=0
        while j<3:
            print(" | ",end="")
            print(k,end="")
            refe[i,j]=k
            k+=1
            j+=1
        i+=1
        print(" | ")
    print("Player 1:- X\nPlayer 2:- O")
    flag=0
    b=0
    while flag!=1:
        flag2=0
        if b>=2:
            flag,move=comp_move(move,magic)
        if flag==0:
            print("Player 1 please enter ",b+1," move:",end="")
            m=int(input())
            i=0
            while i < 3:
                j=0
                while j < 3:
                    if refe[i,j]==m:
                        c=i
                        d=j
                    j+=1
                i+=1
            move[c,d]=1
            while flag2!=1:
                random_integer = random.randint(1, 9)
                i=0
                while i < 3:
                    j=0
                    while j < 3:
                        if refe[i,j]==random_integer:
                            c=i
                            d=j
                        j+=1
                    i+=1
                if move[c,d]!=0 and move[c,d]!=1:
                    print("Player 2 please enter ",b+1," move:",random_integer)
                    move[c,d]=0
                    flag2=1
        print_board(move)
        b+=1
        if b>4:
            flag=1
    if b>4 and flag!=1:
        print("The game is a tie!")

def comp_move(move,magic):
    # X verification:
    flag=verification(move,magic,1)
    # O verification
    if flag==0:
        flag=verification(move,magic,0)
        if flag!=0:
            i=1
            while i <4:
                j=1
                while j<4:
                    if magic[i,j]==flag:
                        a=i
                        b=j
                    j+=1
                i+=1
            if (move[int(a-1),int(b-1)]==1 or move[int(a-1),int(b-1)]==0):
                return 0,move
            p1=vertical(0,move,(b-1))
            p2=horizontal(0,move,(a-1))
            p3=count_occurrences_in_diagonals(0,(a-1),(b-1),move)
            if (p1|p2|p3)==1:
                move[int(a-1),int(b-1)]=0
                print("The algorithm predicts:")
                print_board(move)
                print("Player-2 (O) Wins the game!")
                return 1,move
            else:
                return 0,move
        else:
            return 0,move
    else:
        i=1
        while i <4:
            j=1
            while j<4:
                if magic[i,j]==flag:
                    a=i
                    b=j
                j+=1
            i+=1
        if (move[int(a-1),int(b-1)]==1 or move[int(a-1),int(b-1)]==0):
                return 0,move
        p1=vertical(1,move,(b-1))
        p2=horizontal(1,move,(a-1))
        p3=count_occurrences_in_diagonals(1,(a-1),(b-1),move)
        if (p1|p2|p3)==1:
            move[int(a-1),int(b-1)]=1
            print("The algorithm predicts:")
            print_board(move)
            print("Player-1 (X) Wins the game!")
            return 1,move
        else:
            return 0,move
        

def vertical(y,move,b):
    i=0
    j=b
    count=0
    while i<3:
        if move[i,j]==y:
            count+=1
        i+=1
    if count==2:
        return 1
    else: 
        return 0

def horizontal(y,move,a):
    i=a
    j=0
    count=0
    while j<3:
        if move[i,j]==y:
            count+=1
        j+=1
    if count==2:
        return 1
    else: 
        return 0

def count_occurrences_in_diagonals(element, i, j, array):
    main_diagonal_count = 0
    anti_diagonal_count = 0
    # Count occurrences in the main diagonal
    for k in range(min(len(array), len(array[0]))):
        if 0 <= k < len(array) and 0 <= k < len(array[0]):
            if array[k][k] == element:
                main_diagonal_count += 1
    # Count occurrences in the anti-diagonal
    for k in range(min(len(array), len(array[0]))):
        anti_i = k
        anti_j = len(array[0]) - 1 - k
        if 0 <= anti_i < len(array) and 0 <= anti_j < len(array[0]):
            if array[anti_i][anti_j] == element:
                anti_diagonal_count += 1
    # Check if the element appears twice in both diagonals
    if main_diagonal_count >= 2 or anti_diagonal_count >= 2 or (main_diagonal_count+anti_diagonal_count)>=2:
        return 1
    else:
        return 0

array=np.zeros([5,5])
array[0,:]=array[4,:]=array[:,0]=array[:,4]=-1
array=ms.magic_squre(5,array,1,4,10,1)
tic_tac_toe(array)
