start_game = input("""
                                           |_
                                       ---/ |
                                       ___\_|__
                                      /| o  o |
                       ___           / |______|\          ___
                  ====/___\  ,------,--|------|--.       /___\====
    _________________,|- -|,/---------------------\.____,|- -|,______________
    \                       \. . . . . . . . . . . ./                       /     , 
 ,  \   o           o           o           o           o           o     /    ,   )',    ,     ,(
=)'===\___________________________________________________________________/==="('=='""=='"(=='-'  ',
                            Welcome To Battleship
               <------------------------------------------------->
                Rules:
                The classic battleship game with two phases:
                1. Placement phase: Place your ships on the board.
                First decide the orientation of your ship, then input
                the coordinates.
                The ships can't overlap with eachother.
                There are 5 ships in total:
                1. Carrier: 5 grid
                2. Battleship: 4 grid
                3. Cruiser: 3 grid
                4. Submarine: 3 grid
                5. Destroyer: 2 grid
                --------------------------------------
                2. War phase: The second player will guess the row
                and the column where the ship was placed, 
                if it is a hit, then the player will gain 1 point. 
                The second player got 30 cannonballs.
                If you shoot all of them, then the game is over.
               <-------------------------------------------------> 
                           Press Enter to Continue
""")

while True:
    shootboard=[]
    for i in range(10):
        shootboard.append(["0"]*10)
    board1=[]
    for i in range(10):
        board1.append(["0"]*10)
    ship1=-1  
    ship2=-1

    def shipcheck_u(board,ship1,ship2,n):
        for i in range(1,n+1):
            if  board[ship1-i][ship2-1] == "1":
                print("You can't put your ship here!")
                return 0
            elif board[ship1-(i)][ship2-1] == "1" and i == n:
                print("You can't put your ship here!")
                return 0
            elif board[ship1-(i)][ship2-1] == "0" and i == n:
                return 1
            elif  board[ship1-(i)][ship2-1] == "0":
                continue  

    def shipcheck_d(board,ship1,ship2,n):
        for i in range(2,2+n):
            if  board[(ship1-1)+(i-2)][ship2-1] == "1":
                print("You can't put your ship here!")
                return 0
            elif board[(ship1-1)+(i-2)][ship2-1] == "1" and i == n:
                print("You can't put your ship here!")
                return 0
            elif board[(ship1-1)+(i-2)][ship2-1] == "0" and i == n:
                return 1
            elif  board[(ship1-1)+(i-2)][ship2-1] == "0":
                continue

    def shipcheck_l(board,ship1,ship2,n):
        for i in range(1,n+1):
            if  board[ship1-1][ship2-i] == "1":
                print("You can't put your ship here!")
                return 0
            elif board[ship1-(1)][ship2-i] == "1" and i == n:
                print("You can't put your ship here!")
                return 0
            elif board[ship1-(1)][ship2-i] == "0" and i == n:
                return 1
            elif  board[ship1-(1)][ship2-i] == "0":
                continue  
                
    def shipcheck_r(board,ship1,ship2,n):
        for i in range(2,2+n):
            if  board[ship1-1][(ship2-1)+(i-2)] == "1":
                print("You can't put your ship here!")
                return 0
            elif board[ship1-1][(ship2-1)+(i-2)] == "1" and i == n:
                print("You can't put your ship here!")
                return 0
            elif board[ship1-1][(ship2-1)+(i-2)] == "0" and i == n:
                return 1
            elif  board[ship1-1][(ship2-1)+(i-2)] == "0":
                continue
            
    def shipsize(board,ship1,ship2,n,a):
        for i in range(n):
            if a=="d":
                board[ship1-1][ship2-1]="1"
                ship1+=1
            elif a=="u":
                board[ship1-1][ship2-1]="1"
                ship1-=1
            elif a=="l":
                board[ship1-1][ship2-1]="1"
                ship2-=1
            elif a=="r":
                board[ship1-1][ship2-1]="1"
                ship2+=1

        for row in board:
            print(" ".join(row))
            

    def inputship(board,n):
        a=""
        while a is not "u" and a is not "d" and a is not "l" and a is not "r":
            print("The current ship size is:{0}".format(n))
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
                        shipcheck=shipcheck_u(board,ship1,ship2,n)
                    break
                elif a=="d":
                    while ship1>11-n or ship1<0 or shipcheck==0:
                        shipcheck=0
                        ship1=-1
                        ship1=(int(input("Row coordinate: ")))
                        ship2=-1
                        while ship2>10 or ship2<0:
                            ship2=(int(input("Column coordinate: ")))
                        shipcheck=shipcheck_d(board,ship1,ship2,n)
                    break       
                elif a=="l" :
                    while ship1>10 or ship1<0 or shipcheck==0:
                        shipcheck=0
                        ship1=-1
                        ship1=(int(input("Row coordinate: ")))
                        ship2=-1
                        while ship2<n or ship2>10:
                            ship2=(int(input("Column coordinate: ")))
                        shipcheck=shipcheck_l(board,ship1,ship2,n)
                    break
                elif a=="r":
                    while ship1>10 or ship1<0 or shipcheck==0:
                        shipcheck=0
                        ship1=-1
                        ship1=(int(input("Row coordinate: ")))
                        ship2=-1
                        while ship2>11-n or ship2<0:
                            ship2=(int(input("Column coordinate: ")))
                        shipcheck=shipcheck_r(board,ship1,ship2,n)
                    break
            except ValueError:
                print("Wrong input! Try again!")
        shipsize(board,ship1,ship2,n,a)
        return board
    inputship(board1,5)
    inputship(board1,4)
    for i in range(2):
        inputship(board1,3)
    inputship(board1, 2)
    for i in range(500):
        print("\n")
                        #BATTLE PHASE
def battle_phase(succes, shot):
    n=5
    for i in range(n):  
        while True:
            try:
                guess_column = 0
                guess_row = 0
                while guess_row > 10 or guess_row <= 0 :
                    guess_row = input("Which row you wanna' shoot?('x'=quit): ")
                    if guess_row=="x":
                        quit()
                    else:
                        guess_row = int(guess_row)
                        
                while guess_column > 10 or guess_column <= 0 :
                    guess_column = input("Which column you wanna' shoot?('x'=quit): ")
                    if guess_column=="x":
                        quit()
                    else:
                        guess_column=int(guess_column)

                break
            except (ValueError):
                print("Wrong input!")
        if (board[guess_row-1][guess_column-1] == "1"):
            shot +=1
            success += 1
            board[guess_row-1][guess_column-1] = "x"
            board[guess_row-1][guess_column-1]= "#"
            for row in shootboard:
                print(" ".join(row))
            print("Nice shot!")
            if success==17:
                for row in shootboard:
                    print(" ".join(row))
                print("Congratulations! You destroyed all of the ships! ")
                print("Your score is:{0}".format(success))
                temp=input("Do you want to play again? y/n: ")
                if temp=="y":
                    break
                elif temp=="n":
                    quit()
            else:
                continue
        else: 
            shot +=1
            shootboard[guess_row-1][guess_column-1]= "x"
            for row in shootboard:
                print(" ".join(row))
            print("You missed it!")
        if shot==n:
            print("Game over!")
            print("Your score is:{0}".format(success))
            temp=input("Do you want to play again? y/n: ")
        if temp=="y":
            continue
        elif temp=="n":
            quit()