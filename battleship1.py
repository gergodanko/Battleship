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
        a=str(input('Which way would you like to deploy your ship?\n up="u" down="d" left="l" right="r" \n(or press "x" to quit): '))
        if a=="x":
            quit()
    
    shipcheck=0
    ship1=-1  
    ship2=-1
    while True:
        try:
            if a=="u":
                while ship1<n or ship1<0 or shipcheck==0:
                    shipcheck=0
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    while ship2>10 or ship2<0:
                        ship2=(int(input("Column coordinate: ")))
                    shipcheck=shipcheck_u(ship1,ship2,n)
                break
            elif a=="d":
                while ship1>11-n or ship1<0 or shipcheck==0:
                    shipcheck=0
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    while ship2>10 or ship2<0:
                        ship2=(int(input("Column coordinate: ")))
                    shipcheck=shipcheck_d(ship1,ship2,n)
                break       
            elif a=="l" :
                while ship1>10 or ship1<0 or shipcheck==0:
                    shipcheck=0
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    while ship2<n or ship2>10:
                        ship2=(int(input("Column coordinate: ")))
                    shipcheck=shipcheck_l(ship1,ship2,n)
                break
            elif a=="r":
                while ship1>10 or ship1<0 or shipcheck==0:
                    shipcheck=0
                    ship1=-1
                    ship1=(int(input("Row coordinate: ")))
                    ship2=-1
                    while ship2>11-n or ship2<0:
                        ship2=(int(input("Column coordinate: ")))
                    shipcheck=shipcheck_r(ship1,ship2,n)
                break
        except ValueError:
            print("Wrong input! Try again!")
    shipsize(ship1,ship2,n,a)
    return board1
inputship(5)
inputship(4)
for i in range(2):
    inputship(3)
inputship(2)
for i in range(500):
    print("\n")

success = 0
shot = 0

for i in range(5):
    
    while True:
        try:
            guess_column = 0
            guess_row = 0
            while guess_row > 10 or guess_row <= 0 :
                guess_row = input("Which row you wanna' shoot?: ")
                if guess_row=="x":
                    quit()
                else:
                    guess_row = int(guess_row)
                print(guess_row)
                
            while guess_column > 10 or guess_column <= 0 :
                guess_column = input("Which column you wanna' shoot?: ")
                if guess_column=="x":
                    quit()
                else:
                    guess_column=int(guess_column)

            break
        except (ValueError):
            print("Wrong input!")
    if (board1[guess_row-1][guess_column-1] == "1"):
        shot +=1
        success += 1
        board1[guess_row-1][guess_column-1] = "x"
        board[guess_row-1][guess_column-1]= "#"
        for row in board:
            print(" ".join(row))
        print("Nice shot!")
        if success==17:
            for row in board:
                print(" ".join(row))
            print("Congratulations! You destroyed all of the ships! ")
        else:
            continue
    else: 
        shot +=1
        board[guess_row-1][guess_column-1]= "x"
        for row in board:
            print(" ".join(row))
        print("You missed it!")

print("Game over!")
print("Your score is:{0}".format(success))