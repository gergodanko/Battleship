board=[]
for i in range(10):
    board.append(["0"]*10)
ship1=[]
for i in range(10):
    board.append(["0"]*10)
while True:
    try:
        while ship[0]>5 or ship[0]==0 :
            ship[0]=(int(input("Where should your ship be? Row ")))
        while ship[1]>5 or ship[1]==0:
            ship[1]=(int(input("Where should your ship be? Column")))
        break

    except ValueError:
        print("Wrong input!")
for row in board:
    print(" ".join(row))
print(ship)

