board1=[['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '0', '0', '1', '0'], ['0', '1', '0', '0', '0', '0', '0', '1', '1', '1'], ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'], ['1', '1', '1', '1', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1']]
board=[]

succes = 0
shot = 0
for i in range(10):
    board.append(["0"]*10)
for i in range(5):
    guess_column = 0
    guess_row = 0
    while True:
        try:
            while guess_row > 10 or guess_row <= 0 :
                guess_row = int(input("Which row you wanna' shoot?: "))
            while guess_column > 10 or guess_column <= 0 :
                guess_column = int(input("Which column you wanna' shoot?: "))
        except ValueError:
            print("Wrong input") 
            continue
        break
    if (board1[guess_row-1][guess_column-1] == "1"):
        shot +=1
        succes += 1
        board1[guess_row-1][guess_column-1] = "x"
        board[guess_row-1][guess_column-1]= "#"
        print("Nice shot!")
    else: 
        shot +=1
        print("Miss!")
print("Game over!")
print("Your score is:{0}".format(succes))
print(board1)
