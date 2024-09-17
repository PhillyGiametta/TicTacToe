import random
# <Phillip Giametta>             <12/9/22>
# <TicTacToe Assignment 7>


# Submitting Assignment Note
#When Submitting my file on canvas, it automatically adds a -1 / -2 etc onto the assignment name. I am unsure on how to stop this from happeneing.
#I don't know who will be grading my assignmnet but Professor Holman made a canvas announcement on this issue, and I pasted what he said below.

#Professor Holman's canvas announcement regaurding the issue
#It has been brought to the Instructor's attention that Canvas will change the name of a submission by appending a '-1' or '-2' suffix to it if there is more than one submission attempt. 
#If you have lost points on any of the assignments due to this, it is imperative that you contact your instructor immediately to rectify this problem your grade as it is something that Canvas does on its own.



# PROGRAM INFO
#This program, is a basic implementation of the game TicTacToe. You will take turns choosing squares to put an X in against the Computer (O). 
#By Inputting the number on the square, you will put your mark inside the square. Once a mark is inside the square another person cannot choose the same square.
#The first person to get 3 in a row (across, diagonally etc) wins.
#If no one wins after all spots are full, the game will end in a Tie.

num = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]

def main(): 
    gameOver = False
    print("Welcome to TicTacToe!")
    print()
    
    print("By: <Phillip Giametta>")
    print("[COM S 127 <B>]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 
            stopLoop = False
            currentTurn = 0
            while(stopLoop == False):
                if(currentTurn % 2 == 0):
                    printGameBoard()
                    humanInput = int(input("Choose an INTEGER from 1-9: "))
                    if (humanInput >= 1 and humanInput <= 9 and humanInput in num):
                          updateBoard(humanInput, 'X')
                          num.remove(humanInput)
                          currentTurn +=1  
                    else:                  
                      print("Invalid input. Please try again.")
                else:
                    while(currentTurn != 9):
                        computerI = random.choice(num)
                        print("The Computer Chose: ", computerI)
                        if(computerI in num):
                            num.remove(computerI)
                            updateBoard(computerI, 'O')
                            currentTurn +=1
                            break
                
                winner = Winner(gameBoard)
                if winner == 'X' or winner == 'O':
                  gameOver = "True"
                  stopLoop = "True"
                elif currentTurn == 9:
                  print("The Game Ends In a Tie!")
                  gameOver = "True"
                  stopLoop = "True"
                  break
        

        elif choice == "i":
            print("You are X, The Computer is O. Take turns putting their marks in empty squares.")
            print("The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")
            
        elif choice == "q":
            gameOver = "True"
            print("Goodbye!")
            
            

        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()



def printGameBoard():
  for i in range(3):
    print()
    print("-------------")
    print("|", end="")
    for z in range(3):
      print("", gameBoard[i][z], end=" |")
  print()
  print("-------------")

def updateBoard(input, player):
  input -= 1
  if(input == 0):
    gameBoard[0][0] = player
  elif(input == 1):
    gameBoard[0][1] = player
  elif(input == 2):
    gameBoard[0][2] = player
  elif(input == 3):
    gameBoard[1][0] = player
  elif(input == 4):
    gameBoard[1][1] = player
  elif(input == 5):
    gameBoard[1][2] = player
  elif(input == 6):
    gameBoard[2][0] = player
  elif(input == 7):
    gameBoard[2][1] = player
  elif(input == 8):
    gameBoard[2][2] = player





def Winner(gameBoard):
  for r in range(3):
    c1 = gameBoard[r][0]
    c2 = gameBoard[r][1]
    c3 = gameBoard[r][2]
    if c1 == c2 and c1 == c3 and c2 == c3:
      if c1 == "X":
        printGameBoard()
        print("X has won!")
        return "X"
      else:
        printGameBoard()
        print("O has won!")
        return "O"
  for c in range(3):
    r1 = gameBoard[0][c]
    r2 = gameBoard[1][c]
    r3 = gameBoard[2][c]

    if r1 == r2 and r1 == r3 and r2 == r3:
      if r1 == "X":
        printGameBoard()
        print("X has won!")
        return "X"
      else:
        printGameBoard()
        print("O has won!")
        return "O"
  col = 0
  row = 0
  d1 = gameBoard[row][col]
  d2 = gameBoard[row+1][col+1]
  d3 = gameBoard[row+2][col+2]       
  if d1 == d2 and d1 == d3 and d2 == d3:
    if d1 == "X":
      printGameBoard()
      print("X has won")
      return "X" 
    else:
      printGameBoard()
      print("O has won!")
      return "O"
  col +=2
  dia1 = gameBoard[row][col]
  dia2 = gameBoard[row+1][col-1]
  dia3 = gameBoard[row+2][col-2]
  if dia1 == dia2 and dia1 == dia3 and dia2 == dia3:
    if dia3 == "X":
      printGameBoard()
      print("X has won!")
      return "X"
    else:
      printGameBoard()
      print("O has won!")
      return "O"
  return "KeepPlaying"


if __name__ == "__main__":
    main()



    