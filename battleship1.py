board=[]
for i in range(10):
    board.append(["0"]*10)
board1=[]
for i in range(10):
    board.append(["0"]*10)
while True:
    try:
        while ship:
            ship=(int(input("Where should your ship be? Row ")))
        while ship[1]>5 or ship[1]==0:


    except ValueError:
        print("Wrong input!")
for row in board:
    print(" ".join(row))
print(ship)
