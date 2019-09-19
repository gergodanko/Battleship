board=[]
for i in range(10):
    board.append(["0"]*10)
board1=[]
for i in range(10):
    board1.append(["0"]*10)
ship1=-1  
ship2=-1

def shipcheck_u(ship1,ship2,n):
    for i in range(1,n+1):
        if  board1[ship1-i][ship2-1] == "1":
            print("You can't put your ship here!")
            return 0
        elif board1[ship1-(i)][ship2-1] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board1[ship1-(i)][ship2-1] == "0" and i == n:
            return 1
        elif  board1[ship1-(i)][ship2-1] == "0":
            continue  

def shipcheck_d(ship1,ship2,n):
    for i in range(2,2+n):
        if  board1[ship1+(i-2)][ship2-1] == "1":
            print("You can't put your ship here!")
            return 0
        elif board1[ship1+(i-2)][ship2-1] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board1[ship1+(i-2)][ship2-1] == "0" and i == n:
            return 1
        elif  board1[ship1+(i-2)][ship2-1] == "0":
            continue

def shipcheck_l(ship1,ship2,n):
    for i in range(1,n+1):
        if  board1[ship1-1][ship2-i] == "1":
            print("You can't put your ship here!")
            return 0
        elif board1[ship1-(1)][ship2-i] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board1[ship1-(1)][ship2-i] == "0" and i == n:
            return 1
        elif  board1[ship1-(1)][ship2-i] == "0":
            continue  
            
def shipcheck_r(ship1,ship2,n):
    for i in range(2,2+n):
        if  board1[ship1-1][ship2+(i-2)] == "1":
            print("You can't put your ship here!")
            return 0
        elif board1[ship1-1][ship2+(i-2)] == "1" and i == n:
            print("You can't put your ship here!")
            return 0
        elif board1[ship1-1][ship2+(i-2)] == "0" and i == n:
            return 1
        elif  board1[ship1-1][ship2+(i-2)] == "0":
            continue
        
def shipsize(ship1,ship2,n,a):
    for i in range(n):
        if a=="d":
            board1[ship1-1][ship2-1]="1"
            ship1+=1
        elif a=="u":
            board1[ship1-1][ship2-1]="1"
            ship1-=1
        elif a=="l":
            board1[ship1-1][ship2-1]="1"
            ship2-=1
        elif a=="r":
            board1[ship1-1][ship2-1]="1"
            ship2+=1
    for row in board1:
        print(" ".join(row))
        

def inputship(n):
    a=""
    while a is not "u" and a is not "d" and a is not "l" and a is not "r":
        a=str(input("Milyen irányba álljon a hajo? u,d,l,r"))
    
    shipcheck=0
    ship1=-1  
    ship2=-1
    if a=="u":
        while ship1<n or ship1<0 or shipcheck==0:
            shipcheck=0
            ship1=-1
            ship1=(int(input("Where should your ship be? Row ")))
            ship2=-1
            while ship2>10 or ship2<0:
                ship2=(int(input("Where should you ship be? Column ")))
            shipcheck=shipcheck_u(ship1,ship2,n)

    elif a=="d":
        while ship1>11-n or ship1<0 or shipcheck==0:
            shipcheck=0
            ship1=-1
            ship1=(int(input("Where should your ship be? Row ")))
            ship2=-1
            while ship2>10 or ship2<0:
                ship2=(int(input("Where should you ship be? Column ")))
            shipcheck=shipcheck_d(ship1,ship2,n)
                
    elif a=="l" :
        while ship1>10 or ship1<0 or shipcheck==0:
            shipcheck=0
            ship1=-1
            ship1=(int(input("Where should your ship be? Row ")))
            ship2=-1
            while ship2<n or ship2>10:
                ship2=(int(input("Where should you ship be? Column ")))
            shipcheck=shipcheck_l(ship1,ship2,n)

    elif a=="r":
        while ship1>10 or ship1<0 or shipcheck==0:
            shipcheck=0
            ship1=-1
            ship1=(int(input("Where should your ship be? Row ")))
            ship2=-1
            while ship2>11-n or ship2<0:
                ship2=(int(input("Where should you ship be? Column ")))
            shipcheck=shipcheck_r(ship1,ship2,n)

    shipsize(ship1,ship2,n,a)
    return board1
inputship(5)
inputship(4)
for i in range(2):
    inputship(3)
inputship(2)
for row in board1:
    print(" ".join(row))