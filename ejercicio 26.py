print("welcome to Rock, paper and scissors")
print("enter 1 for the rock / enter 2 for the papper / enter 3 for the scissors")

player1 = int(input(" player 1... enter your desicion: "))
player2 = int(input(" player 2...enter your desicion: "))

if player1 == 1 and player2 == 2:
    print("the player 2 won")
elif player1 == 2 and player2 == 3:
    print("the player 2 won")
elif player1 == 1 and player2 == 3: 
    print("the player 1 won")
elif player1 == 2 and player2 == 3:
    print("the player 2 won")
else: 
    print("what is your desicion?")