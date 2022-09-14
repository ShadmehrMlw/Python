from random import randint

import random
print("Rock...")
print("Paper...")
print("Scissors...")

randomNumber = random.randint(0,2)
ComputerMove = "Rock"

if randomNumber == 0:
    ComputerMove = "Rock"
elif randomNumber == 1:
    ComputerMove = "Paper"
elif randomNumber == 2:
    ComputerMove = "Scissors"

Player1_Wins = 0
Player2_Wins = 0
WininigScre = 4
while Player1_Wins < WininigScre and Player2_Wins < WininigScre :
    print(f"Player1_Wins : {Player1_Wins} and Player2_Wins : {Player2_Wins}")
    Player_1 = input("Player_1 Make your move : ")
    print(f"Player_2 Make your move : {ComputerMove}")
    Player_2 = ComputerMove
    if Player_1 == "Quit" or Player_1 == "quit" or Player_1 == "QUIT" :
        break
    if Player_1 == Player_2:
        print("Thats a tie...")

    elif Player_1 == "Rock":
        if Player_2 == "Scissors":
            print("Player_1 Wins!...")
            Player1_Wins +=1
        elif Player_2 == "Paper":
            print("Player_2 Wins!...")
            Player2_Wins +=1 
    elif Player_1 == "Paper":
        if Player_2 == "Scissors":
            print("Player_2 Wins!...")
            Player2_Wins +=1
        elif Player_2 == "Rock":
            print("Player_1 Wins!...")
            Player1_Wins +=1
    elif Player_1 == "Paper":
        if Player_2 == "Rock":
            print("Player_1 Wins!...")
            Player1_Wins +=1
        elif Player_2 == "Scissors":
            print("Player_2 Wins!...")
            Player2_Wins +=1
    elif Player_1 == "Scissors":
        if Player_2 == "Paper":
            print("Player_1 Wins!...")
            Player1_Wins +=1
        elif Player_2 == "Rock":
            print("Player_2 Wins!...")
            Player2_Wins +=1
            
    else:
        print("Somthing went wrong")
print(f"Player1 final score : {Player1_Wins} and Player2 final score : {Player2_Wins}")

# if Player_1 == "Rock" and Player_2 == "Scissors":
#     print("Player_1 Wins!...")
# elif Player_1 == "Rock" and Player_2 == "Paper":
#     print("Player_2 Wins!...")
# elif Player_1 == "Paper" and Player_2 == "Rock":
#     print("Player_1 Wins!...")
# elif Player_1 == "Paper" and Player_2 == "Scissors":
#     print("Player_2 Wins!...")
# elif Player_1 == "Scissors" and Player_2 == "Paper":
#     print("Player_1 Wins!...")
# elif Player_1 == "Scissors" and Player_2 == "Rock":
#     print("Player_2 Wins!...")

# elif Player_1 == Player_2:
#     print("Thats a tie...")
# else:
#     print("Somthing went wrong")
