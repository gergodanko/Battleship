board=[]
for i in range(10):
    board.append(["0"]*10)
board1=[]
for i in range(10):
    board1.append(["0"]*10)


while True:
    try:
        ship1=-1  
        ship2=-1
        a=""
        a=str(input("Milyen irányba álljon a hajo? u,d,l,r"))
        if a=="u":
            while ship1<5 or ship1<0:
                ship1=(int(input("Where should your ship be? Row ")))
        elif a=="d":
            while ship1>5 or ship1<0:
                ship1=(int(input("Where should your ship be? Row ")))
        elif a=="l" or a=="r":
            while ship1>10 or ship1<0:
                ship1=(int(input("Where should your ship be? Row ")))
        if a=="u" or a=="d":
            while ship2>10 or ship2<0:
                ship2=(int(input("Where should you ship be? Column ")))
        elif a=="l":
            while ship2<5 or ship2>10:
                ship2=(int(input("Where should you ship be? Column ")))
        elif a=="r":
            while ship2>5 or ship2<0:
                ship2=(int(input("Where should you ship be? Column ")))
        for i in range(5):
            if a=="u":
                board1[ship1][ship2]="1"
                ship1-=1
            elif 
        break

    except ValueError:
        print("Wrong input!")
#for i in range(5):
   # board1[ship1][ship2]="1"
    #ship1+=1

for row in board1:
    print(" ".join(row))
#for row in board:
 #   print(" ".join(row))

