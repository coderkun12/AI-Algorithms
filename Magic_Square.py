import numpy as np

def magic_squre(siz,array,low_b,up_b,lim,low):
    num=low
    array[int(1),int(siz//2)]=num
    i=1
    j=(siz//2)
    num+=1
    while num <=(lim-1):
        if array[int(i-1),int(j+1)] != -1:
            if array[int(i-1),int(j+1)]==0:
                array[int(i-1),int(j+1)]=num
                i=(i-1)
                j=(j+1)
                num+=1
            elif array[int(i+1),int(j)]==0:
                array[int(i+1),int(j)]=num
                i=(i+1)
                num+=1
        else:
            if (((i-1)<low_b) and ((j+1)>up_b-1)):
                if array[int(up_b-1),int(1)]!=0:
                    array[int(i+1),j]=num
                    num+=1
                    i=i+1
                else:
                    array[int(up_b-1),int(1)]=num
                    num+=1
                    j=1
                    i=up_b-1
            elif ((((i-1)<=up_b-1) and ((i-1)>=low_b)) and (j+1>up_b-1)):
                array[int(i-1),int(low_b)]=num
                num+=1
                i=i-1
                j=low_b
            elif (((i-1)<low_b) and (((j+1)>=low_b) and ((j+1)<=(up_b-1)))):
                array[int(up_b-1),int(j+1)]=num
                j=j+1
                i=up_b-1
                num+=1
    print(array[low_b:up_b,low_b:up_b])

n = int(input("Enter the dimension:"))
if n%2 != 0:
    array=np.zeros([n+2,n+2])
    sizee=n+2
    low=int(input("Enter lower end number:"))
    array[0,:]=-1 
    array[sizee-1,:]=-1
    array[:,0]=-1
    array[:,sizee-1]=-1
    low_bound=1
    up_bound=(sizee-1)
    lim=(n**2)+low
    magic_squre(n+2,array,low_bound,up_bound,lim,low)
else:
    print("Enter an odd dimension, please!")