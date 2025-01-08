import random
op1='TWO'
res='FOUR'
print("  T  W  O")
print("+")
print("  T  W  O")
print("----------")
print("F  O  U  R")
print("----------")
flag=0
while flag!=1:
    dictt={}
    dictt['F']=1
    li=[]
    li.append(1)
    for i in range(len(op1)-1,-1,-1):
        if op1[i]!='T':
            val=random.randint(2,9)
            while val in li:
                val=random.randint(2,9)
            dictt[op1[i]]=val
            dictt[res[i+1]]=(val+val)%10
            li.append(val)
            li.append((val+val%10))
        else:
            val=random.randint(5,9)
            while val in li:
                val=random.randint(5,9)
            dictt[op1[i]]=val
            li.append(val)
            if res[i+1]=='O':
                if dictt['O']==val+val or dictt['O']==((val+val)%10):
                    flag=1
                    dictt[res[i+1]]=(val+val)%10
                    li.append((val+val)%10)
print("\nFor above cryptoarithmetic we get following values of the characters to satisfy the constraints:\n",dictt)
