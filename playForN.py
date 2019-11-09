"""
@author: Nayem
"""

import math
import random


n=int(input("Play for "))
print("###########")
n_count=int(math.sqrt(n))+2
com=[]
hum=[]
s=0
com_win=0
hum_win=0
draw=0
turn=1
w=0
l=0
fp=0
ran=int(n/4)+4
for i in range(n_count):
    com.append(random.randint(1,ran))
    hum.append(random.randint(1,ran))

com.sort()
hum.sort()

def showScore():
    print("Current value ",s)
    print("Computer -->",com)
    print("You ------->",hum)
    
def gameEnd():
    if(len(com)==0 and len(hum)==0):
        print("*** DRAW ***")
        return True
    elif(s<n):
        return False
    elif(n==s):
        if(turn==2):
            print("*** CPU wins ***")
        else:
            print("*** YOU win ***")
    else:
        if(turn==1):
            print("*** CPU wins ***")
        else:
            print("*** YOU win ***")
    return True


def evaluate(move,count,comRemain,humRemain):
    global w
    global l
    global fp
    if(move==2):
        if(count==n):
            w=w+1
            return True
        elif(count>n):
            fp=-1
            return False
        
    else:
        if(count==n):
            l=l+1
            return True
        elif(count>n):
            fp=1
            return False
    if(move==1):
        f1=0
        for i in range(len(comRemain)):
            temp=comRemain[i]
            comRemain.remove(temp)
            m1=evaluate(2,count+temp,comRemain,humRemain)
            if(m1):
                f1=1
            comRemain.append(temp)
            comRemain.sort()
        if(f1==0):
            l=l+1
    else:
        f2=0
        for i in range(len(humRemain)):
            temp=humRemain[i]
            humRemain.remove(temp)
            m2=evaluate(1,count+temp,comRemain,humRemain)
            if(m2):
                f2=1
            humRemain.append(temp)
            humRemain.sort()
        if(f2==0):
            w=w+1
    return False
            


def comMove():
    global w
    global l
    global s
    global fp
    chance=-1
    valToMove=-1
    for i in range(len(com)):
        w=0
        l=0
        temp = com[i]
        com.remove(temp)
        m=evaluate(2,s+temp,com,hum)
        if(m==False):
            if fp==-1:
                l=l+1
                fp=0
            elif fp==1:
                w=w+1
                fp=0
        com.append(temp)
        com.sort()

        probability =(w*100)/(w+l)
        if(probability>chance):
            chance=probability
            valToMove=temp
    print("CPU moved :",valToMove)
    s=s+valToMove
    com.remove(valToMove)
    
        
        
def humMove():
    val=int(input("Your turn :"))
    global s
    s+=val
    hum.remove(val)

while 1:
    showScore()
    if(gameEnd()):
        break;
    elif(turn==1):
        comMove()
        turn=2
    else:
        humMove()
        turn=1
        
    
    
    
    
    