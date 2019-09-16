board=[]
for i in range(10):
    board.append(["0"]*10)
board1=[]
for i in range(10):
    board1.append(["0"]*10)
print(board1)

#while True:
    #try:
ship1=-1  
ship2=-1
while ship1>10 or ship1<0:
    ship1=(int(input("Where should your ship be? Row ")))
while ship2>10 or ship2<0:
    ship2=(int(input("Where should you ship be? Column ")))
    #except ValueError:
        #print("Wrong input!")
for i in range(5):
    board1[ship1][ship2]="1"
    ship1+=1

for row in board1:
    print(" ".join(row))
#for row in board:
 #   print(" ".join(row))

