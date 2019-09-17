board=[]
for i in range(10):
    board.append(["0"]*10)
board1=[]
for i in range(10):
    board1.append(["0"]*10)
ship1=-1  
ship2=-1
def shipcheck_u(ship1,ship2,n):
    for i in range(n):
        print(board1[ship1-1-i][ship2-1-i])
        if  board1[ship1-1-i][ship2-1-i] == "1":
            return False
        elif board1[ship1-1-i][ship2-1-i] == "0" and i == n-1:
            return True
        elif  board1[ship1-1-i][ship2-1-i] == "0":
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
        

def inputship(n):
    a=""
    while a is not "u" and a is not "d" and a is not "l" and a is not "r":
        a=str(input("Milyen irányba álljon a hajo? u,d,l,r"))
    
    ship1=-1  
    ship2=-1
    if a=="u":
        while ship1<n or ship1<0 and shipcheck==False:
            ship1=(int(input("Where should your ship be? Row ")))
            shipcheck = shipcheck_u(ship1,ship2,n)
    elif a=="d":
        while ship1>10-n or ship1<0:
            ship1=(int(input("Where should your ship be? Row ")))
    elif a=="l" or a=="r":
        while ship1>10 or ship1<0:
            ship1=(int(input("Where should your ship be? Row ")))
    if a=="u" or a=="d":
        while ship2>10 or ship2<0:
            ship2=(int(input("Where should you ship be? Column ")))
    elif a=="l":
        while ship2<n or ship2>10:
            ship2=(int(input("Where should you ship be? Column ")))
    elif a=="r":
        while ship2>10-n or ship2<0:
            ship2=(int(input("Where should you ship be? Column ")))
    shipsize(ship1,ship2,n,a)
    return board1
inputship(5)
inputship(4)
for i in range(2):
    inputship(3)
inputship(2)
for row in board1:
    print(" ".join(row))
